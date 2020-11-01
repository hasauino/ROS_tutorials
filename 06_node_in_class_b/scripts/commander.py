#! /usr/bin/env python
import rospy
from util import Turtle

if __name__ == "__main__":
    t1 = Turtle()

    r = 1.0  # m
    w = 1.0  # rad/sec

    v = w*r  # m/s

    while not rospy.is_shutdown():
        t1.set_velocity(v, w)
        print ('-------------')
        print (t1.color)
