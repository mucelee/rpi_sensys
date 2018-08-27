import requests
import json 
import httplib

from entity import Entity 
from entityAttribute import EntityAttribute

from Template.jsonConvert import JsonConvert

NGSI_VERSION_2 = "/v2/entities/" 
NGSI_ATTR = "/attrs"

HEADERS = {"Content-Type" : "application/json"}

# umschreiben https://github.com/evandempsey/python-design-patterns/blob/master/patterns/observer.py
class Observer(object):
    """
    Abstract class to respond to changes in the subject.
    """
    def Update(self, instance, attributesDict):
        """
        Update observer state.
        """
        raise NotImplementedError("publish() is not implemented.")

class EntityAttributeChangeObserver(Observer):
    def __init__(self, fiwareAddress):
        self.fiwareAddress = fiwareAddress
    
    def Update(self, instance, attributesDict):
        id = instance.__class__.__name__ + "1"
        # shame on me, a really dirty, workaround!
        asJson = '{"'
        for key in iter(attributesDict):
            asJson += key  +'" :' + EntityAttribute(attributesDict[key]).toJson()
        asJson += '}'
        print asJson
        response = requests.patch(self.fiwareAddress +NGSI_VERSION_2  + str(id) + NGSI_ATTR , data=asJson, headers=HEADERS)
        statusCode = response.status_code
        print statusCode

