from Template.Fiware.sensorDataEntry import SensorDataEntry

class InfraredSensor(SensorDataEntry):

    def __init__(self):
        SensorDataEntry.__init__(self)
        self.test = 0

    def test_value_change(self):
        self.test += 1
