#! /usr/bin/env python
import rospy
from util import Turtle

if __name__ == "__main__":

    rospy.init_node('my_node')
    t1 = Turtle()

    r = rospy.get_param('radius', default=1.0)
    w = rospy.get_param('ang_speed', default=1.0)

    v = w*r  # m/s

    while not rospy.is_shutdown():
        t1.set_velocity(v, w)
