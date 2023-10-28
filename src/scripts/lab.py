import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, TeleportRelative
import termios
import sys
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
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ord(ch)

def move_turtle():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    rospy.init_node('turtle_keyboard_control', anonymous=True)
    rospy.wait_for_service('/turtle1/teleport_absolute')
    teleport_absolute = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
    rospy.wait_for_service('/turtle1/teleport_relative')
    teleport_relative = rospy.ServiceProxy('/turtle1/teleport_relative', TeleportRelative)

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
            print("Reseteando la posición de la tortuga.")
            teleport_absolute(5.54444599152, 5.54444599152, 0.0)
        elif key == SPACE:
            print("Realizando un giro de 180 grados.")
            teleport_relative(0.0, 0.0, pi)

        pub.publish(twist)
        rate.sleep()

if _name_ == '_main_':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass
