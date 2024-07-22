#!/usr/bin/env python3





from functools import partial
import random
import math
import rclpy
from rclpy.node import Node
import sys

from turtlesim.srv import Spawn
from turtlesim.srv import Kill
from tutorial_interfaces.msg import Turtle
from tutorial_interfaces.msg import TurtleArray
from tutorial_interfaces.srv import CatchTurtle
from std_msgs.msg import Int16


class MinimalService(Node):

    def __init__(self):
        super().__init__('turtle_create')
        self.number_of_turtles = int(sys.argv[1])
        self.turtle_name_prefix_ = "turtle"
        self.turtle_counter_ = 1
        self.alive_turtles_ = []
        self.alive_turtles_publisher_ = self.create_publisher(
            TurtleArray, "alive_turtles", 10)
        self.counts_turtles_publisher_ = self.create_publisher(
            Int16, "turtle_count", 10)
        
        self.spawn_turtle_timer_ = self.create_timer(
            2.0, self.spawn_new_turtle)
        self.catch_turtle_service_ = self.create_service(
            CatchTurtle, "catch_turtle", self.callback_catch_turtle)

    def callback_catch_turtle(self, request, response):
        self.call_kill_server(request.name)
        response.success = True
        return response


    def spawn_new_turtle(self):
        self.turtle_counter_ += 1
        if self.turtle_counter_ == self.number_of_turtles + 1:
            rclpy.shutdown()
        name = self.turtle_name_prefix_ + str(self.turtle_counter_)
        x = random.uniform(0.0, 11.0)
        y = random.uniform(0.0, 11.0)
        theta = random.uniform(0.0, 2*math.pi)
        self.call_spawn_server(name, x, y, theta)

    def call_spawn_server(self, turtle_name, x, y, theta):
        client = self.create_client(Spawn, "spawn")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Server...")

        request = Spawn.Request()
        request.x = x
        request.y = y
        request.theta = theta
        request.name = turtle_name

        future = client.call_async(request)
        future.add_done_callback(
            partial(self.callback_call_spawn, turtle_name=turtle_name, x=x, y=y, theta=theta))

    def callback_call_spawn(self, future, turtle_name, x, y, theta):
        try:
            response = future.result()
            if response.name != "":
                self.get_logger().info("Turtle " + response.name + " is now alive")
                new_turtle = Turtle()
                new_turtle.name = response.name
                new_turtle.x = x
                new_turtle.y = y
                new_turtle.theta = theta
                self.alive_turtles_.append(new_turtle)
                self.publish_alive_turtles()
                count = Int16()
                count.data = self.turtle_counter_
                self.counts_turtles_publisher_.publish(count)
        except Exception as e:
            self.get_logger().error("Service call failed %r" % (e,))
    def publish_alive_turtles(self):
        msg = TurtleArray()
        msg.turtles = self.alive_turtles_
        self.alive_turtles_publisher_.publish(msg)
    
  
def main(args=None):
    rclpy.init(args=args)

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()

if __name__ == '__main__':
    main()