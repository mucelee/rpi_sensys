import requests
import json 
import httplib
import time
import threading

from SAN.Serialization.entity import Entity
from Utilities.jsonConvert import JsonConvert


HEADERS = {"Content-Type" : "application/json"}

def isResponseOk(statusCode):
    if(statusCode >= httplib.OK and statusCode <= httplib.IM_USED): # everything is fine
        return True
    return False

class ContextBrokerHandler:

    verboseLogging = False

    def __init__(self, fiwareAddress, minSendInterval=0.1):
        self.fiwareAddress = fiwareAddress
        self.minSendInterval = minSendInterval
        self._published_entities = []
        self._attached_entities = []
        self._start_loop()

    def attach_entity(self, entity):
        self._attached_entities.append(entity)

    def register_entities(self):
        for entity in self._attached_entities:
            self._create_entity(entity)

    def unregister_entities(self):
        for entity in self._published_entities:
            self._delete_entity(entity)

    #region Private methods

    def _start_loop(self):
        print("Starting entity observer thread...")
        updateThread = threading.Thread(target=self._loop)
        updateThread.start()

    def _loop(self):
        while True:
            time.sleep(self.minSendInterval)
            for entity in self._published_entities:
                if(entity.is_dirty() == True):
                    self._update_entity(entity)

    def _create_entity(self, entityInstance):
        print "Creating entity %s" % (entityInstance.id)
        # Delete the old entity if wasn't shut down properly
        if(self._delete_entity(entityInstance)):
            print "Error deleting the old entity in context broker!"
        entity = Entity(entityInstance)
        jsonString = JsonConvert.ToJSON(entity)
        if self.verboseLogging:
            print jsonString
        response = requests.post("%s/v2/entities" % (self.fiwareAddress), data=jsonString, headers=HEADERS)
        if(isResponseOk(response.status_code)): # everything is fine
            self._published_entities.append(entityInstance)
            print "Entity created"
        elif(response.status_code == httplib.BAD_REQUEST): # everything is NOT fine
            print "UNPROCESSABLE_ENTITY"
            print json.loads(response.content)
        else:
            print json.loads(response.content)

    def _update_entity(self, entityInstance):
        print "Update entity %s" % (entityInstance.id)
        entity = Entity(entityInstance)
        jsonString = JsonConvert.ToJSON(entity)
        jsonString = ContextBrokerHandler._remove_id_and_type(jsonString)
        if self.verboseLogging:
            print jsonString
        response = requests.patch("%s/v2/entities/%s/attrs" % (self.fiwareAddress, entity.id), data=jsonString, headers=HEADERS)
        if isResponseOk(response.status_code): # everything is fine
            entityInstance.clear_dirty()
            print "Updated entity"
        elif response.status_code == httplib.BAD_REQUEST: # everything is NOT fine
            print "UNPROCESSABLE_ENTITY"
            print json.loads(response.content)
        else:
            print json.loads(response.content)

    def _delete_entity(self, entity):
        print "Deleting entity %s" % (entity.id)
        response = requests.delete("%s/v2/entities/%s" % (self.fiwareAddress, entity.id))
        if(isResponseOk(response.status_code)): # everything is fine
            print "Status OK"
            if entity in self._published_entities: # Not sure at all about this, probably shouldn't delete on creation and don't need that check
                self._published_entities.remove(entity)
            return 0
        else:
            print json.loads(response.content)
            return response.status_code

    @staticmethod
    def _remove_id_and_type(jsonString):
        jsonObject = json.loads(jsonString)
        del jsonObject["id"]
        del jsonObject["type"]
        return json.dumps(jsonObject, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    #endregion