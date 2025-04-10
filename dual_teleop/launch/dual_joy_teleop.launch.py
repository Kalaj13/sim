import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    nodes = []

    # Always include joy for controller 1 (ego_racecar)
    nodes.append(
        Node(
            package='joy',
            executable='joy_node',
            name='joy_node_ego',
            parameters=[{'dev': '/dev/input/js0'}],
            output='screen',
        )
    )

    nodes.append(
        Node(
            package='teleop_twist_joy',
            executable='teleop_node',
            name='joy_ego',
            parameters=[{
                'axis_linear': 1,
                'axis_angular': 2,
                'scale_linear': 1.5,
                'scale_angular': 2.0,
                'enable_button': 5,
                'require_enable_button': True,
            }],
            remappings=[('/cmd_vel', '/cmd_vel')]
        )
    )

    nodes.append(
        Node(
            package='dual_teleop',
            executable='twist_to_ackermann_node',
            name='twist_to_ackermann_ego',
            parameters=[{
                'input_topic': '/cmd_vel',
                'output_topic': '/drive',
            }]
        )
    )

    # Check if second joystick is available
    if os.path.exists('/dev/input/js1'):
        nodes.append(
            Node(
                package='joy',
                executable='joy_node',
                name='joy_node_opp',
                namespace='joy2',
                parameters=[{'dev': '/dev/input/js1'}],
                output='screen',
            )
        )

        nodes.append(
            Node(
                package='teleop_twist_joy',
                executable='teleop_node',
                name='joy_opp',
                namespace='joy2',
                parameters=[{
                    'axis_linear': 1,
                    'axis_angular': 2,
                    'scale_linear': 1.5,
                    'scale_angular': 2.0,
                    'enable_button': 5,
                    'require_enable_button': True,
                    'joy_config': 'xbox'
                }],
                remappings=[('/cmd_vel', '/cmd_vel_opp')],
                arguments=['--ros-args', '--remap', '/joy:=/joy2/joy']
            )
        )

        nodes.append(
            Node(
                package='dual_teleop',
                executable='twist_to_ackermann_node',
                name='twist_to_ackermann_opp',
                parameters=[{
                    'input_topic': '/cmd_vel_opp',
                    'output_topic': '/opp_drive',
                }]
            )
        )

    return LaunchDescription(nodes)
