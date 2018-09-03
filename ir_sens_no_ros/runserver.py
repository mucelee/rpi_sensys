from os import environ
import time

from Template.configParser import Config

# local imports
from Template.Fiware.sensorAgentNode import SensorAgentNode
from InfraredSensor.infraredSensor import InfraredSensor

from Template.Fiware.contextBrokerHandler import ContextBrokerHandler
from Template.Fiware.entitiyObserver import EntityAttributeChangeObserver

HOST = '0.0.0.0'
PORT = 5555
SERVER_ADDRESS = "localhost"

CONFIG_FILE = "fiware_config.ini"
parsedConfigFile = Config(CONFIG_FILE)

if __name__ == '__main__': 
    # create an instance of the fiware ocb handler
    ocbHandler = ContextBrokerHandler(parsedConfigFile.getFiwareServerAddress())
    
    sensorAgentNode = SensorAgentNode()
    irSensor = InfraredSensor()
    sensorAgentNode.add_sensor(irSensor) 
    
    # before registering/publishing the entities, attaching is required
    # after adding it to the ocbHandler, feel free to register/publish the entities
    ocbHandler.attach_entity(sensorAgentNode)
    ocbHandler.register_entities()

    user_input = ""
    while True:
        irSensor.test_value_change()
        time.sleep(0.1)
        pass
    while user_input!= "exit":
        user_input = raw_input("-->")
    print "Done"
    ocbHandler.unregister_entities()
    #SubscribtionHandler.unsubscribeContext(parsedConfigFile)    
