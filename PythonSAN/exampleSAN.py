from os import environ
import time

from Utilities.configParser import Config
from SAN.sensorAgentNode import SensorAgentNode
from SAN.contextBrokerHandler import ContextBrokerHandler

from Example.exampleSensor import ExampleSensor
from Example.exampleSensorTimeseries import ExampleSensorTimeseries
import Example.exampleAlternative as exampleAlternative

CONFIG_FILE = "fiware_config.ini"
parsedConfigFile = Config(CONFIG_FILE)

if __name__ == '__main__':
    # Optionally set verbose logging of json data
    ContextBrokerHandler.verboseLogging = False

    # Create an instance of the Fiware OCB handler
    ocbHandler = ContextBrokerHandler(parsedConfigFile.getFiwareServerAddress())
    # Create SAN instance
    sensorAgentNode = SensorAgentNode()
    
    # Create sensor and add to SAN
    
    # Example 1
    #exampleSensor = ExampleSensor()
    #sensorAgentNode.add_sensor(exampleSensor)

    # Example 2
    #exampleSensorTimeseries = ExampleSensorTimeseries()
    #sensorAgentNode.add_sensor(exampleSensorTimeseries)
    
    # Example 3
    exampleAlternative.startLoop()
    sensorAgentNode.add_sensor(exampleAlternative.sensor) 
    
    
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
