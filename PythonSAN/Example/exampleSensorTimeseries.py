import time
import datetime
import threading

from SAN.sensorDataEntry import SensorDataEntry

class ExampleSensorTimeseries(SensorDataEntry):

    def __init__(self):
        SensorDataEntry.__init__(self)
        self._lastReading = 0
        threading.Thread(target=self.loop).start()

    def loop(self):
        self._nextPublishTime = 0
        while True:
           time.sleep(0.25)
           self.test_value_change() 

    def test_value_change(self):    
        self._lastReading += 1
        self.addReading(self._lastReading, True)
        if time.time() > self._nextPublishTime:
            self._nextPublishTime = time.time() + 10
            self.set_dirty()

    @property
    def sensorId(self):
        return "testId"

    @property
    def sensorType(self):
        return "testType"

    @property
    def measurementType(self):
        return "testMeasurementType"