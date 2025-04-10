import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from ackermann_msgs.msg import AckermannDriveStamped

class DualJoyTeleop(Node):
    def __init__(self):
        super().__init__('dual_joy_teleop')

        self.publisher_ego = self.create_publisher(AckermannDriveStamped, '/drive', 10)
        self.publisher_opp = self.create_publisher(AckermannDriveStamped, '/opp_drive', 10)

        self.create_subscription(Joy, '/joy1', self.joy1_callback, 10)
        self.create_subscription(Joy, '/joy2', self.joy2_callback, 10)

        self.get_logger().info('Dual joystick teleop started')

    def joy1_callback(self, msg):
        drive_msg = self.convert_joy_to_drive(msg)
        self.publisher_ego.publish(drive_msg)

    def joy2_callback(self, msg):
        drive_msg = self.convert_joy_to_drive(msg)
        self.publisher_opp.publish(drive_msg)

    def convert_joy_to_drive(self, joy_msg):
        drive_msg = AckermannDriveStamped()
        drive_msg.drive.speed = joy_msg.axes[1] * 2.0  # Forward/back
        drive_msg.drive.steering_angle = joy_msg.axes[3] * 0.34  # Left/right
        return drive_msg

def main(args=None):
    rclpy.init(args=args)
    node = DualJoyTeleop()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
