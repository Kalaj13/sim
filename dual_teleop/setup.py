from setuptools import setup

package_name = 'dual_teleop'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/dual_joy_teleop.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yourname',
    maintainer_email='your@email.com',
    description='Dual joystick control for F1TENTH',
    license='MIT',
    entry_points={
        'console_scripts': [
            'twist_to_ackermann_node = dual_teleop.twist_to_ackermann_node:main',
        ],
    },
)

