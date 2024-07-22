#!/usr/bin/env python3
import math
import rclpy
from functools import partial
import rclpy.logging
from rclpy.node import Node

from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from tutorial_interfaces.msg import Turtle
from tutorial_interfaces.msg import TurtleArray
from tutorial_interfaces.srv import CatchTurtle
import numpy as np
import math
import time
from std_msgs.msg import Int16


class TurtleControllerNode(Node):
    def __init__(self):
        super().__init__("turtle_controller")

        self.turtle1pose = Pose()
        self.turtle2pose = Pose()
        self.vel_msg = Twist()
        self.catch_closest_turtle_first_ = True
        self.turtle_to_catch_ = None
        self.turtle_count_ = 0
        self.distance_tolerance = float(input("Set your tolerance: "))
        
        
        self.cmd_vel_publisher_ = self.create_publisher(
            Twist, "turtle2/cmd_vel", 10)

        self.turtle2pose_subscriber_ = self.create_subscription(
            Pose, "turtle2/pose", self.callback2, 10)
        
        
        self.turtle1pose_subscriber_ = self.create_subscription(
            Pose, "turtle1/pose", self.callback1, 10)
        
        #self.alive_turtles_subscriber_ = self.create_subscription(
        #    TurtleArray, "alive_turtles", self.callback_alive_turtles, 10)
        self.counts_turtles_subscriber_ = self.create_subscription(
            Int16, "turtle_count",self.turtlescount, 10)
        
    def turtlescount(self,data):
        self.turtle_count_ = data.data
        self.get_logger().info('turtle count: "%d"' % self.turtle_count_)

    

                    

    def callback1(self,msg):
        self.turtle1pose = msg
        self.get_logger().info('turtle1 pose: "%s"' % self.turtle1pose)
    
    def callback2(self,msg):
        self.turtle2pose = msg
        self.get_logger().info('turtle2 pose: "%s"' % self.turtle2pose)
        self.move2goal()


    
    
        

    def euclidean_distance(self, goal_pose):
        """Euclidean distance between current pose and the goal."""
        return math.sqrt(math.pow((goal_pose.x - self.turtle2pose.x), 2) +
                     math.pow((goal_pose.y - self.turtle2pose.y), 2))
    def linear_vel(self, goal_pose, constant=0.5):
    #     """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
         return constant * self.euclidean_distance(goal_pose)
 
    def steering_angle(self, goal_pose):
    #     """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
         return math.atan2(goal_pose.y - self.turtle2pose.y, goal_pose.x - self.turtle2pose.x)
 
    def angular_vel(self, goal_pose, constant=1.2):
    #     """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
         return constant * (self.steering_angle(goal_pose) - self.turtle2pose.theta)
 
    def move2goal(self):
    
 
         # Please, insert a number slightly greater than 0 (e.g. 0.01).
 
         
         if self.euclidean_distance(self.turtle1pose) >= self.distance_tolerance:
             #print(self.euclidean_distance(goal_pose))
             # Porportional controller.
             # https://en.wikipedia.org/wiki/Proportional_control
 
             # Linear velocity in the x-axis.
             self.vel_msg.linear.x = self.linear_vel(self.turtle1pose)
             self.vel_msg.linear.y = 0.0
             self.vel_msg.linear.z = 0.0
 
             # Angular velocity in the z-axis.
             self.vel_msg.angular.x = 0.0
             self.vel_msg.angular.y = 0.0
             self.vel_msg.angular.z = self.angular_vel(self.turtle1pose)
 
             # Publishing our vel_msg
             self.cmd_vel_publisher_.publish(self.vel_msg)
             time.sleep(0.5)
             
 
 
         # Stopping our robot after the movement is over.
         self.vel_msg.linear.x = 0.0
         self.vel_msg.angular.z = 0.0
         self.cmd_vel_publisher_.publish(self.vel_msg)
 
         # If we press control + C, the node will stop.

    



def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()