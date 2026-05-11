#!/usr/bin/env python

import rospy
from services_test.srv import server


rospy.init_node('move_trg_srvc')
rospy.wait_for_service('/move_trg')

service = rospy.ServiceProxy('/move_trg',server)
side = int(input('direction: '))
repetition = float(input('speed:'))

esult = service(side, repetition)

print (result.success)
