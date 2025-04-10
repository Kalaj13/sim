from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='joy',
            executable='joy_node',
            name='joy_node1',
            namespace='',
            parameters=[{'dev': '/dev/input/js0'}],
            remappings=[('/joy', '/joy1')],
        ),
        Node(
            package='joy',
            executable='joy_node',
            name='joy_node2',
            namespace='',
            parameters=[{'dev': '/dev/input/js1'}],
            remappings=[('/joy', '/joy2')],
        ),
        Node(
            package='dual_teleop',
            executable='dual_joy_to_drive',
            name='dual_joy_teleop_node',
            output='screen'
        )
    ])
