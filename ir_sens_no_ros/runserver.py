from os import environ
import time

from Template.configParser import Config

# local imports
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
    entityAttributeChangePublisher = EntityAttributeChangeObserver(parsedConfigFile.getFiwareServerAddress())
    irSensor = InfraredSensor()
    # before registering/publishing the entities, attaching is required
    ocbHandler.attach_entity(irSensor)
    # after adding it to the ocbHandler, feel free to register/publish the entities
    ocbHandler.register_entities()
    irSensor.attach_publisher(entityAttributeChangePublisher)
    print "Done"
    user_input = ""
    while user_input!= "exit":
        user_input = raw_input("-->")
    ocbHandler.unregister_entities()
    #SubscribtionHandler.unsubscribeContext(parsedConfigFile)    
