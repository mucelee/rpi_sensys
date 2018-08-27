import entityAttribute

class Sensor(object):
    def __init__(self, _object):
        self.__dict__.clear()
        for key, value in _object.__dict__.iteritems():
             print key, value
             if (str(key).startswith('_', 0, 1)):
                pass
             else:
                self.__dict__[key] = entityAttribute.EntityAttribute(value, {})

    def __repr__(self):
        return ""#Id: " + str(self.sensorId) + ", Type: " + str (self.sensorType)
