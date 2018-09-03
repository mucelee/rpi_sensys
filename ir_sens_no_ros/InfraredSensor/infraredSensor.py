from Template.Fiware.sensorDataEntry import SensorDataEntry

class InfraredSensor(SensorDataEntry):

    def __init__(self):
        SensorDataEntry.__init__(self)
        self.test = 0

    def test_value_change(self):
        self.test += 1
    
    """ def __repr__(self):
        retVal = ""
        retVal = "Type: " + str(self.__class__.__name__)
        return retVal """
