from turtlesimmulakatpy.srv import TurtleCreate  
import rclpy
from rclpy.node import Node


class MinimalService(Node):

    def __init__(self):
        super().__init__('turtle_create')
        self.srv = self.create_service(TurtleCreate, 'add_more_turtles', self.add_more_turtles_callback)        # CHANGE

    def dd_more_turtles_callback(self, request, response):
        response.name = request.x + request.y + request.theta + request.name                                                  # CHANGE
        self.get_logger().info('Incoming request\na: %d b: %d c: %d name: %s' % (request.x, request.y, request.theta)) # CHANGE

        return response

def main(args=None):
    rclpy.init(args=args)

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()

if __name__ == '__main__':
    main()