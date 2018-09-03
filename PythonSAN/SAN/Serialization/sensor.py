import entityAttribute

class Sensor(object):
    def __init__(self, _object):
        self.__dict__.clear()
        self.sensorId = entityAttribute.EntityAttribute(_object.sensorId, {})
        self.sensorType = entityAttribute.EntityAttribute(_object.sensorType, {})
        self.measurementType = entityAttribute.EntityAttribute(_object.measurementType, {})
        self.readings = entityAttribute.EntityAttribute(_object.readings, {})
        # for key, value in _object.__dict__.iteritems():
        #     if str(key).startswith('_', 0, 1):
        #         pass
        #     else:
        #         self.__dict__[key] = entityAttribute.EntityAttribute(value, {})
