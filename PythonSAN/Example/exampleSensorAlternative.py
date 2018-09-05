import time

from SAN.sensorDataEntry import SensorDataEntry

class ExampleSensorAlternative(SensorDataEntry):

    @property
    def sensorId(self):
        return "testAltId"

    @property
    def sensorType(self):
        return "testAltType"

    @property
    def measurementType(self):
        return "testAltMeasurementType"