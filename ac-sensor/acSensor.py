#!/usr/bin/env python
import ads1256
import math
import time
import threading

from SAN.sensorDataEntry import SensorDataEntry

class AlternatingCurrentSensor(SensorDataEntry):

	# configuration
	adcChannel = 2
	publishInterval = 1
	readFrequency = 30000 # ADC's SPS parameter. Possible values:   2d5,  5,  10,  15,  25,  30,  50,  60,  100,  500,  1000,  2000,  3750,  7500,  15000,  30000
	smoothingFactor = 0.05
	minimumDeltaMilliampsForPublish = 0

	def __init__(self):
		SensorDataEntry.__init__(self)
		self.voltageAverage = 0
		self.voltagePositiveAverage = 0
		#self.lastPublishedCurrent = -999999
		self.nextPublishTime = 0
		if ads1256.start("1",str(self.readFrequency)) != 0:
			print "Failed starting ADC"
			return
		threading.Thread(target=self.loop).start()

	def __del__(self):
		ads1256.stop()

	def loop(self):
		while True:
			nextProcessTime = time.time() + 1.0 / self.readFrequency / 2.0
			self.processData(ads1256.read_all_channels()[self.adcChannel])
			while time.time() < nextProcessTime:
				pass
			#time.sleep(1 / self.readFrequency / 2)

	def processData(self, channelValue):
		voltage = ((channelValue * 100) / 167.0) / 1000000.0
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
