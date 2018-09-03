from sensorReading import SensorReading

class SensorDataEntry(object):

    def __init__(self):
        print("Initializing sensor: %s" % (self.__class__.__name__))
        self._isDirty = False
        self.readings = []

    def is_dirty(self):
        return self._isDirty

    def set_dirty(self):
        self._isDirty = True

    def clear_dirty(self):
        self._isDirty = False
        del self.readings[:]

    def addReading(self, reading, timeseries=False):
        if not timeseries:
            del self.readings[:]
        self.readings.append(SensorReading(reading))

    @property
    def sensorId(self):
        raise NotImplementedError()

    @property
    def sensorType(self):
        raise NotImplementedError()

    @property
    def measurementType(self):
        raise NotImplementedError()