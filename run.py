import paho.mqtt.client as mqtt
import time

Msg = ' '  

def on_message(client, userdata, msg):
	if msg.topic == '/123456789/l4ms/san_1/attrs/stat':
		globMsg = msg.payload
		splitMsg = globMsg.split('	')
		Msg = splitMsg[0]
		client.publish("/123456789/san_1_data/attrs/acttim",Msg)
		Msg = splitMsg[1]
		client.publish("/123456789/san_1_data/attrs/speed",Msg)
		Msg = splitMsg[2]
		client.publish("/123456789/san_1_data/attrs/psent",Msg)
		Msg = splitMsg[3]
		client.publish("/123456789/san_1_data/attrs/prec",Msg)
		Msg = splitMsg[4]
		client.publish("/123456789/san_1_data/attrs/ram",Msg)
		
	elif msg.topic == '/123456789/l4ms/san_1/attrs/sw':
		globMsg = msg.payload
		client.publish("/123456789/san_1_switch/attrs/sw",globMsg)
		
	elif msg.topic == '/123456789/l4ms/san_1/attrs/link':
		globMsg = msg.payload
		client.publish("/123456789/san_1_data/attrs/link",globMsg)
			
def on_disconnect(client, userdata,rc=0):
    logging.debug("DisConnected result code "+str(rc))
    client.loop_stop()

client = mqtt.Client()
client.on_message = on_message
client.connect("192.168.0.104", 1883, 60)

client.loop_start()
client.subscribe("/123456789/l4ms/#")

while True: 
	time.sleep(1)

	


