#! /usr/bin/env python


import rospy

rospy.init_node('my_node')

param = rospy.get_param('name', default="channel")

print (param)

rospy.set_param('age', 20)
