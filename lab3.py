#!/usr/bin/env python
#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, TeleportRelative
import termios
import sys
import os
from numpy import pi

# Definir las teclas
W = 119  # Tecla 'w'
S = 115  # Tecla 's'
A = 97   # Tecla 'a'
D = 100  # Tecla 'd'
R = 114  # Tecla 'r'
SPACE = 32  # Tecla de espacio

def get_key():
    # Obtener la tecla presionada
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        key = ord(sys.stdin.read(1))
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return key

def move_turtle():
    rospy.init_node('turtle_keyboard_control', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        twist = Twist()
        key = get_key()

        if key == W:
            twist.linear.x = 1.0
        elif key == S:
            twist.linear.x = -1.0
        elif key == D:
            twist.angular.z = -1.0
        elif key == A:
            twist.angular.z = 1.0
        elif key == R:
            teleport_absolute(5.54444599152, 5.54444599152, 0.0)
        elif key == SPACE:
            teleport_relative(0.0, 0.0, pi)

        pub.publish(twist)
        rate.sleep()

if __name__ == '__main__':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass
