import json 

fiwareDatatypePrimitives = [float, int, str]

class EntityAttribute():
    """description of class"""
    def __init__(self, _object):
        self.value = _object;
        self.type = ""
        self.metadata = {}
        objectType = type(_object)

        if(objectType is float):
            self.type = "Float"
            self.value = float(_object)
        elif objectType is int:
            self.type = "Integer"
            self.value = int(_object)
        elif objectType is str:
            self.type = "String"
            self.value = str(_object)
        elif objectType is list:
            self.type = "Array"
            self.value = []
            for item in _object:
                self.value.append(EntityAttribute(item))
        elif objectType is bool:
            self.type = "Boolean"
            self.value = bool(_object)
            
        else:
            self.type = _object.__class__.__name__
            tempDict = {}
            for key, value in _object.__dict__.iteritems():
                tempDict[key] = EntityAttribute(value)
            self.value = tempDict

    def toJson(self):
       # return json.dumps(self.__dict__)
       #return json.dumps(dict(type =self.type, value =self.value))
       return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def __str__(self):
        return self.toJson()

    def __repr__(self):
        return self.toJson()