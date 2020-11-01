#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist


class Turtle:
    def __init__(self):
        rospy.init_node('turtle')
        self.__pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1)
        self.__vel_msg = Twist()

    def set_velocity(self, v, w):
        self.__vel_msg.linear.x = v
        self.__vel_msg.angular.z = w
        self.__pub.publish(self.__vel_msg)
