#!/usr/bin/env python
import ads1256
import time
import rospy
from std_msgs.msg import Float32

def ReadValues():
	rate = 25 # Frequency in Hz
	
	ads1256.start("1",str(rate))
	pub = rospy.Publisher('/sen_4/ResVal', Float32, tcp_nodelay=False, queue_size=1)
	rospy.init_node('Rheostat',anonymous=True)
	rate=rospy.Rate(10)
	while not rospy.is_shutdown():
		absoluteValue = ads1256.read_channel(0)
		voltage = ((absoluteValue*100)/167.0)/1000000.0
		rospy.loginfo(voltage)
		pub.publish(voltage)
		rate.sleep()
	ads1256.stop()
	
if __name__== '__main__':
	try:
		ReadValues()
	except rospy.ROSInterruptException:
		pass
