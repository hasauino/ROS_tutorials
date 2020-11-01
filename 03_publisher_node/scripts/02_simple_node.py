import rospy


rospy.init_node('node1')
rate = rospy.Rate(1)

while not rospy.is_shutdown():
    print ("warshat best channel")
    rate.sleep()
