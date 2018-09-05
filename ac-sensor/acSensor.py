#!/usr/bin/env python
import ads1256
import math
import time
import threading

from SAN.sensorDataEntry import SensorDataEntry

class AlternatingCurrentSensor(SensorDataEntry):

	# configuration
	adcChannel = 4
	publishInterval = 1
	gain = 1 # ADC Gain. Possible values : 1, 2, 4, 8, 16, 32, 64 - shouldnt use anything but 1, unless we find a decent library for the ADC chip and can set a vref or create more complex circuit to bring baseline to 0V
	readFrequency = 30000 # ADC's SPS parameter. Possible values:   2d5,  5,  10,  15,  25,  30,  50,  60,  100,  500,  1000,  2000,  3750,  7500,  15000,  30000
	smoothingFactor = 0.25
	#minimumDeltaMilliampsForPublish = 0

	def __init__(self):
		SensorDataEntry.__init__(self)
		self.voltageAverage = 0
		self.voltagePositiveAverage = 0
		#self.lastPublishedCurrent = -999999
		self.nextPublishTime = 0
		if ads1256.start(str(self.gain), str(self.readFrequency)) != 0:
			print "Failed starting ADC"
			return
		self.stopLoop = False
		threading.Thread(target=self.loop).start()

	def __del__(self):
		ads1256.stop()
		self.stopLoop = True
		print "Destroying sensor"

	def loop(self):
		while not self.stopLoop:
			#nextProcessTime = time.time() + 0.02 #1.0 / self.readFrequency * 2
			self.processData(ads1256.read_all_channels()[self.adcChannel])
			#self.processData(ads1256.read_channel(self.adcChannel))
			#while time.time() < nextProcessTime:
			#	pass
			#waitTime = nextProcessTime - time.time()
			#print waitTime
			time.sleep(0.01) # let other threads work

	def processData(self, channelValue):
		voltage = ((channelValue * 100) / 167.0) / 1000000.0 / self.gain
		if(self.voltageAverage == 0):
			self.voltageAverage = voltage
			self.voltagePositiveAverage = voltage
		else:
			self.voltageAverage = voltage * self.smoothingFactor + self.voltageAverage * (1 - self.smoothingFactor)
			if(voltage > self.voltageAverage):
				self.voltagePositiveAverage = voltage * self.smoothingFactor + self.voltagePositiveAverage * (1 - self.smoothingFactor)
		rmsMillivolts = (self.voltagePositiveAverage - self.voltageAverage) * 1000 # voltage on the ends of coil
		rmsMilliamps = math.floor(rmsMillivolts * 30)
		# if math.fabs(self.lastPublishedCurrent - rmsMilliamps) < self.minimumDeltaMilliampsForPublish:
		# 	return
		# print(rmsMilliamps)
		currentTime = time.time()
		if currentTime < self.nextPublishTime:
			return
		print(rmsMilliamps)
		self.nextPublishTime = currentTime + 1
		self.lastPublishedCurrent = rmsMilliamps
		self.addReading(rmsMilliamps)
		self.set_dirty()

	@property
	def sensorId(self):
		return "ac_1"

	@property
	def sensorType(self):
		return "AC Sensor"

	@property
	def measurementType(self):
		return "RMS Current Milliamperes"
