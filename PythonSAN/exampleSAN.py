from os import environ
import time

from Utilities.configParser import Config
from SAN.sensorAgentNode import SensorAgentNode
from SAN.contextBrokerHandler import ContextBrokerHandler

from Example.exampleSensor import ExampleSensor
from Example.exampleSensorTimeseries import ExampleSensorTimeseries

CONFIG_FILE = "fiware_config.ini"
parsedConfigFile = Config(CONFIG_FILE)

if __name__ == '__main__':
    # Optionally set verbose logging of json data
    ContextBrokerHandler.verboseLogging = False

    # Create an instance of the Fiware OCB handler
    ocbHandler = ContextBrokerHandler(parsedConfigFile.getFiwareServerAddress())
    # Create SAN instance
    sensorAgentNode = SensorAgentNode()
    
    # Create sensor and add to SAN (Use one or both)
    #exampleSensor = ExampleSensor()
    exampleSensorTimeseries = ExampleSensorTimeseries()
    sensorAgentNode.add_sensor(exampleSensorTimeseries) 
    
    
    # Attach SAN to OCB handler
    ocbHandler.attach_entity(sensorAgentNode)
    # Register entities with OCB server
    ocbHandler.register_entities()

    # Keep running until user Ctrl+C's
    try:
	    while True:
		    pass
    except KeyboardInterrupt:
        pass
    print "Done"
    # Delete entities after shutting down
    ocbHandler.unregister_entities()   
