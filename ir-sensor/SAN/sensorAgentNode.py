import datetime
import time
import threading
import sys

from baseFiwareClass import BaseFiwareClass

class SensorAgentNode(BaseFiwareClass):
    
    _metadata_modifiedTime = {"timeFormat": "ISO8601"}

    def __init__(self):
        BaseFiwareClass.__init__(self)
        self.id = "SAN_demo" # get unique ID later
        self.type = "SensorAgent"
        self.sensorData = []
        self._isDirty = False

    @property
    def modifiedTime(self):
        return datetime.datetime.now().isoformat()

    def add_sensor(self, sensor):
        if(sensor not in self.sensorData):
            self.sensorData.append(sensor)

    def remove_sensor(self, sensor):
        if(sensor in self.sensorData):
            self.sensorData.remove(sensor)

    def is_dirty(self):
        if self._isDirty: 
            return True
        for sensor in self.sensorData:
            if sensor.is_dirty():
                return True
        return False

    def clear_dirty(self):
        for sensor in self.sensorData:
            sensor.clear_dirty()
        BaseFiwareClass.clear_dirty(self)
