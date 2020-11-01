import rospy
from std_msgs.msg import String


def cb(msg):
    print (msg.data)


rospy.init_node('mostame3')

rospy.Subscriber('myTopic', String, callback=cb)

while not rospy.is_shutdown():
    pass
