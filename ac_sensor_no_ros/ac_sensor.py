#!/usr/bin/env python
import ads1256
import time
import math
import os

ip = os.getenv('FIWARE_IP', '192.168.0.110')
port = os.getenv('FIWARE_PORT', '7896')
apiKey = os.getenv('FIWARE_API_KEY', '1234')
deviceId = os.getenv('FIWARE_DEVICE_ID', 'san_2_ac_sensor')
attributeName = os.getenv('FIWARE_ATTRIBUTE_NAME', 'coilVoltage')
requestData = 'http://%s:%s/iot/d?k=%s&i=%s&d=%s|{}' % (ip, port, apiKey, deviceId, attributeName)

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
	rmsMillivolts = math.floor((voltagePositiveAverage - voltageAverage) * 1000) # voltage on the ends of coil
	uri = requestData.format(rmsMillivolts)
	print(uri)
	#requests.post(uri, headers={"context-type":"text/plain"})

def ReadValues():
	while True:
		Loop(ads1256.read_channel(adcChannel))
		time.sleep(1 / readFrequency / 2)
	ads1256.stop()
	
if __name__== '__main__':
	try:
		ReadValues()
	except KeyboardInterrupt:
		ads1256.stop()
		pass

ads1256.stop()
