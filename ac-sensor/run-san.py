import os
import time
import sys

from Utilities.configParser import Config
from SAN.sensorAgentNode import SensorAgentNode
from SAN.contextBrokerHandler import ContextBrokerHandler

from acSensor import AlternatingCurrentSensor

CONFIG_FILE = "fiware_config.ini"
parsedConfigFile = Config(CONFIG_FILE)

if __name__ == '__main__':
    # Optionally set verbose logging of json data
    ContextBrokerHandler.verboseLogging = False

    # Create an instance of the Fiware OCB handler
    ocbHandler = ContextBrokerHandler(parsedConfigFile.getFiwareServerAddress(), 1)
    # Create SAN instance
    sensorAgentNode = SensorAgentNode()

    # Create sensor
    acSensor = AlternatingCurrentSensor()
    sensorAgentNode.add_sensor(acSensor)

    # Attach SAN to OCB handler
    ocbHandler.attach_entity(sensorAgentNode)
    # Register entities with OCB server
    ocbHandler.register_entities()

    # Keep running until user Ctrl+C's
    try:
        while True:
            pass
    except KeyboardInterrupt:
        del acSensor
        del sensorAgentNode
        ocbHandler.unregister_entities()
        del ocbHandler
	os._exit(os.EX_OK)
    print "Done"
