#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Bool
import RPi.GPIO as GPIO
from time import sleep

IN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(IN,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def sen_3():
	ct = 0
	pub = rospy.Publisher('/sen_3/IrSensor', Bool, queue_size=1)
	
	rospy.init_node('IRSensor',anonymous=True)
	rate=rospy.Rate(1)
	while not rospy.is_shutdown():
		if(GPIO.input(IN) == 1 and ct == 1):
			rospy.loginfo(1)
			pub.publish(1)
			ct = 0
		elif(GPIO.input(IN) == 0 and ct == 0):
			pub.publish(0)
			rospy.loginfo(0)
			ct = 1
			
		rate.sleep()
		
	
if __name__== '__main__':
	try:
		sen_3()
	except rospy.ROSInterruptException:
		pass


