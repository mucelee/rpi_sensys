#!/usr/bin/env python
import ads1256
import time
import math
import rospy
from std_msgs.msg import Float32

# configuration #
adcChannel = 2
publishInterval = 1
readFrequency = 30000 # ADC's SPS parameter. Possible values:   2d5,  5,  10,  15,  25,  30,  50,  60,  100,  500,  1000,  2000,  3750,  7500,  15000,  30000
smoothingFactor = 0.01
#################

voltageAverage = 0
voltagePositiveAverage = 0
nextPublishTime = 0
ads1256.start("1",str(readFrequency))
pub = rospy.Publisher('/sen_4/ac_sensor', Float32, tcp_nodelay=False, queue_size=1)
rospy.init_node('ac_sensor', anonymous=True)
rate=rospy.Rate(readFrequency / 2)

def Loop(channelValue):
	global voltageAverage, voltagePositiveAverage, nextPublishTime
	voltage = ((channelValue*100)/167.0)/1000000.0
	if(voltageAverage == 0):
		voltageAverage = voltage
		voltagePositiveAverage = voltage
	else:
		voltageAverage = voltage * smoothingFactor + voltageAverage * (1 - smoothingFactor)
		if(voltage > voltageAverage):
			voltagePositiveAverage = voltage * smoothingFactor + voltagePositiveAverage * (1 - smoothingFactor)
	currentTime = time.clock()
	if(currentTime < nextPublishTime):
		return
	
	nextPublishTime = currentTime + publishInterval
	rmsMillivolts = math.floor((voltagePositiveAverage - voltageAverage) * 1000)
	rospy.loginfo(rmsMillivolts)
	pub.publish(rmsMillivolts)

def ReadValues():
	while not rospy.is_shutdown():
		Loop(ads1256.read_channel(adcChannel))
		rate.sleep()
	ads1256.stop()
	
if __name__== '__main__':
	try:
		ReadValues()
	except rospy.ROSInterruptException:
		ads1256.stop()
		pass

ads1256.stop()
