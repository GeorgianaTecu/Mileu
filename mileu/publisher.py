#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32
rospy.init_node('simple_publisher')
pub = rospy.Publisher('/cmd_vel',Twist , queue_size=1)

rate = rospy.Rate(10)
mg = 
