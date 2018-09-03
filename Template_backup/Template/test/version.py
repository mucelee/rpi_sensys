from peter import Peter 

class Version():
    """description of class""" 
    def __init__(self):
        self.version = 1
        self.StringTest = "pd"
        self.IntegerTest = "20180428" 
        self.ArrayTest = [2, "3", 3.1, Peter()] 
        self.FloatTest = 3.4
        self.BooleanTest = True
        self.ObjectTest = Peter()

        self.ObjectArrayTest = [Peter()] * 4;
    
    def toJson(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return self.toJson()
        