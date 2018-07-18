#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Bool
import RPi.GPIO as GPIO
from time import sleep

IN = 18
ct = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(IN,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def sen_2():
	global ct
	pub = rospy.Publisher('/sen_2/buttonState', Bool, queue_size=1)
	
	rospy.init_node('ButtSender',anonymous=True)
	rate=rospy.Rate(.5)
	while not rospy.is_shutdown():
		if(GPIO.input(18) == 1 and ct == 0):
			rospy.loginfo(1)
			pub.publish(1)
			ct=1
		elif(GPIO.input(18) == 0 and ct == 1):
			pub.publish(0)
			ct-=1
			
		rate.sleep()
		
	
if __name__== '__main__':
	try:
		sen_2()
	except rospy.ROSInterruptException:
		pass


