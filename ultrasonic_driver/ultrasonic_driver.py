import rclpy
import time
from rclpy.node import Node
from std_msgs.msg import String

from .hardware_interface import distance

class UltrasonicPublisher(Node):

    def __init__(self):
        super().__init__('ultrasonic_publisher')
        self.publisher_ = self.create_publisher(String, 'ultrasonic/distance', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = String()
        wall = distance()
        msg.data = f"Distance: {wall} cm"
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)

    ultrasonic_publisher = UltrasonicPublisher()

    rclpy.spin(ultrasonic_publisher)

    ultrasonic_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
