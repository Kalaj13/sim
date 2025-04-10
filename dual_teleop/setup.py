from setuptools import setup

package_name = 'dual_teleop'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/dual_teleop.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='you',
    maintainer_email='your@email.com',
    description='Dual joystick teleop for f1tenth_gym_ros',
    license='MIT',
    entry_points={
        'console_scripts': [
            'dual_joy_to_drive = dual_teleop.dual_joy_to_drive:main',
        ],
    },
)
