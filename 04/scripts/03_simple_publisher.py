import rospy
from std_msgs.msg import String

rospy.init_node('node2')

pub = rospy.Publisher('myTopic',  String, queue_size=10)
rate = rospy.Rate(1)



my_msg = String()

my_msg.data = "warshat best channel"

while not rospy.is_shutdown():
    pub.publish(my_msg)
    rate.sleep()
    