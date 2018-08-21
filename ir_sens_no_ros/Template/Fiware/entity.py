from entityAttribute import EntityAttribute
"""
- More Information: https://www.fiware.org/wp-content/uploads/2016/12/2_FIWARE-NGSI-Managing-Context-Information-at-large-scale.pdf
Entity consits of
    - EntityId
    - EntityType
    - has n Attributes:
        - Name
        - Type
        - Value
        has n-Metadata:
            - Name
            - Type
            - Value
"""

VERSION = "1"


class Entity(object):
    def __init__(self):
        self.type = self.__class__.__name__
        self.id = self.type 

    def convertObjectToEntity(self, _object):
        self.__dict__.clear() 
        # thats how to set the type and id of an entity - its simple but works for a first version
        if not _object.id == None:
            self.id = _object.id
        else:
            self.id = self.type + VERSION
        self.type  = _object.type #_object.__class__.__name__
        
        if(hasattr(_object, "modifiedTime")):
            self.modifiedTime = EntityAttribute(_object.modifiedTime(), _object._metadata_modifiedTime)
        else:
            print("No modified time defined for object")

        for key, value in _object.__dict__.iteritems():
             print key, value
             if (key == "type" or key =="id" or str(key).startswith('_', 0, 1)):
                pass
             else:
                self.__dict__[key] = EntityAttribute(value)
    
 
    def __repr__(self):
        retVal = ""
        retVal = "Id: " + str(self.id) + ", Type: " + str (self.type)
        return retVal


def validateAndConvertValues(polValues):
    newArray = []
    for item in polValues:
        newVal = int(item) if isValidPollTime(item) else -1
        newArray.append(newVal)
    return newArray