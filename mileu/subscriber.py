#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist
def callback(msg):
	print(msg.data)

rospy.init_node('simple_subscriber')
sub=rospy.Subscriber('/scan', Int32, callback)

rospy.spin()
