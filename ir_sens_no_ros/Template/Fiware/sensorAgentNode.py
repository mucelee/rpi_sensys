import datetime
from baseFiwareClass import BaseFiwareClass
#from sensorDataEntry import SensorDataEntry

class SensorAgentNode(BaseFiwareClass):
    _metadata_modifiedTime = {"timeFormat": "ISO8601"}
    _sensors = []

    def __init__(self):
        self.id = "SAN_demo" # get unique ID later
        self.type = "SensorAgent"

    def modifiedTime(self):
        return datetime.datetime.now().isoformat()

    def add_sensor(self, sensor):
        if(sensor not in self._sensors):
            self._sensors.append(sensor)

    def remove_sensor(self, sensor):
        if(sensor in self._sensors):
            self._sensors.remove(sensor)