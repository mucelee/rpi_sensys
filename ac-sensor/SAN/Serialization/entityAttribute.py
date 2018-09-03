import json

from SAN.sensorDataEntry import SensorDataEntry
from SAN.sensorReading import SensorReading
import sensor
import reading

class EntityAttribute():
    def __init__(self, _object, metadata=None):
        objectType = type(_object)
        # Floats
        if(objectType is float):
            self.type = "Float"
            self.value = float(_object)
        # Ints
        elif objectType is int:
            self.type = "Integer"
            self.value = int(_object)
        # Strings
        elif objectType is str:
            self.type = "String"
            self.value = str(_object)
        # Booleans
        elif objectType is bool:
            self.type = "Boolean"
            self.value = bool(_object)
        # Lists/Arrays
        elif objectType is list:
            self.type = "Array"
            self.value = []
            for item in _object:
                # Sensors
                if isinstance(item, SensorDataEntry):
                    self.value.append(sensor.Sensor(item))
                # Readings
                elif isinstance(item, SensorReading):
                    self.value.append(reading.Reading(item))
                # Generic objects
                else:
                    self.value.append(EntityAttribute(item))
        # Dictionaries
        elif objectType is dict:
            for key, value in _object.iteritems():
                setattr(self, key, EntityAttribute(value))
        # Other objects
        else:
            self.type = _object.__class__.__name__
            tempDict = {}
            for key, value in _object.__dict__.iteritems():
                tempDict[key] = EntityAttribute(value)
            self.value = tempDict
        # Add metadata
        if(metadata != None):
            self.metadata = EntityAttribute(metadata)

    def toJson(self):
       return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def __str__(self):
        return self.toJson()

    def __repr__(self):
        return self.toJson()