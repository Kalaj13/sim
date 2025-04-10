import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from ackermann_msgs.msg import AckermannDriveStamped

class TwistToAckermann(Node):
    def __init__(self):
        super().__init__('twist_to_ackermann')

        self.declare_parameter('input_topic', '/cmd_vel')
        self.declare_parameter('output_topic', '/drive')

        input_topic = self.get_parameter('input_topic').get_parameter_value().string_value
        output_topic = self.get_parameter('output_topic').get_parameter_value().string_value

        self.subscription = self.create_subscription(Twist, input_topic, self.cmd_callback, 10)
        self.publisher = self.create_publisher(AckermannDriveStamped, output_topic, 10)

    def cmd_callback(self, msg):
        drive_msg = AckermannDriveStamped()
        drive_msg.drive.speed = msg.linear.x
        drive_msg.drive.steering_angle = msg.angular.z
        self.publisher.publish(drive_msg)

def main(args=None):
    rclpy.init(args=args)
    node = TwistToAckermann()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
