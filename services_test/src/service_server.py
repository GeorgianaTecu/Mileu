#!/usr/bin/env python

import rospy
from services_test.srv import server
from geometry_msgs.msg import Twist 

def callback(request):
    cmd = Twist()
    mileu = request.repetitions
    end_time = rospy.Time.now() + rospy.Duration(side)

    for i in range (mileu):
        for i in range (3):
            cmd.linear.x = 0.5
            cmd.angular.z = 0.2 
            while rospy.Time.now() < end_time:
                pub.publish(cmd)
        
    return True



rospy.init_node('move_trg')
service_srv = rospy.Service('/move_trg', server, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)
rospy.spin()
