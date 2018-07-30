import RPi.GPIO as GPIO
from time import sleep
import requests
import os

gpioPin = int(os.getenv('GPIO_PIN', 23))
ip = os.getenv('FIWARE_IP', '192.168.0.110')
port = os.getenv('FIWARE_PORT', '7896')
apiKey = os.getenv('FIWARE_API_KEY', '1234')
deviceId = os.getenv('FIWARE_DEVICE_ID', 'san_2_ir_sensor')
attributeName = os.getenv('FIWARE_ATTRIBUTE_NAME', 'objectPresence')
requestData = 'http://%s:%s/iot/d?k=%s&i=%s&d=%s|{}' % (ip, port, apiKey, deviceId, attributeName)

print(requestData.format("true"))

lastSentState = -1

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpioPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def san_2():
	global lastSentState, requestData

	if(GPIO.input(gpioPin) == 1 and lastSentState != 1):
		lastSentState = 1
		requests.post(requestData.format("true"), headers={"context-type":"text/plain"})
		print("TRUE")
	elif(GPIO.input(gpioPin) == 0 and lastSentState != 0):
		lastSentState = 0
		requests.post(requestData.format("false"), headers={"context-type":"text/plain"})
		print("FALSE")
	sleep(1)

try:
	while True:
		san_2()
except KeyboardInterrupt:
	requests.post(requestData.format("false"), headers={"context-type":"text/plain"})
	GPIO.cleanup()
