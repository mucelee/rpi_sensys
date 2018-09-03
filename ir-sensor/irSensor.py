import RPi.GPIO as GPIO
import time
import threading

from SAN.sensorDataEntry import SensorDataEntry

gpioPin = 23

class IrSensor(SensorDataEntry):

	def __init__(self):
		SensorDataEntry.__init__(self)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(gpioPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		self._objectPresence = None
		threading.Thread(target=self.loop).start()

	def __del__(self):
		GPIO.cleanup()
		
	def loop(self):
		while True:
			time.sleep(0.01)
			currentObjectPresence = GPIO.input(gpioPin) == 1
			if self._objectPresence != currentObjectPresence:
				self._objectPresence = currentObjectPresence
				self.addReading(currentObjectPresence)
				self.set_dirty()

	@property
	def sensorId(self):
		return "ir_1"

	@property
	def sensorType(self):
		return "IR Sensor"

	@property
	def measurementType(self):
		return "Object Presence"