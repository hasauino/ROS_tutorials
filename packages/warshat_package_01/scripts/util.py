#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.msg import Color


class Turtle:
    def __init__(self):
        self.__pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1)
        rospy.Subscriber('turtle1/pose', Pose, callback=self.__cb_pose)
        rospy.Subscriber('/turtle1/color_sensor', Color,
                         callback=self.__cb_color)
        self.__vel_msg = Twist()
        self.pose = [0., 0., 0.]
        self.color = Color()

    def set_velocity(self, v, w):
        self.__vel_msg.linear.x = v
        self.__vel_msg.angular.z = w
        self.__pub.publish(self.__vel_msg)

    def __cb_pose(self, msg):
        self.pose[0] = msg.x
        self.pose[1] = msg.y
        self.pose[2] = msg.theta

    def __cb_color(self, msg):
        self.color = msg
