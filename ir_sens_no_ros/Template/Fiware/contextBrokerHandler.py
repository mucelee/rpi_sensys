import requests
import json 
import httplib
import time
import threading

from entity import Entity 
from entityAttribute import EntityAttribute

from Template.jsonConvert import JsonConvert


HEADERS = {"Content-Type" : "application/json"}

def isResponseOk(statusCode):
    if(statusCode >= httplib.OK and statusCode <= httplib.IM_USED): # everything is fine
        return True
    return False

class ContextBrokerHandler:

    def __init__(self, fiwareAddress):
        self._fiwareAddress = fiwareAddress
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
        print("start_loop")
        updateThread = threading.Thread(target=self._update_loop)
        updateThread.start()

    def _update_loop(self):
        while True:
            time.sleep(1)
            print(".")
            for entity in self._published_entities:
                if(entity.is_dirty() == True):
                    self._update_entity(entity)

    def _create_entity(self, entityInstance):
        print "Create Entity"
        statusCode = httplib.OK

        # check maybe to delete:
        if(self._delete_entity(entityInstance)):
            print "error"

        entity = Entity()
        entity.convertObjectToEntity(entityInstance)
        
        jsonString = JsonConvert.ToJSON(entity)
        print jsonString

        response = requests.post(self._fiwareAddress + "/v2/entities", data=jsonString, headers=HEADERS)
        statusCode = response.status_code
        if(isResponseOk(statusCode)): # everything is fine
            self._published_entities.append(entityInstance)
            print "Status OK"
        elif(statusCode == httplib.BAD_REQUEST): # everything is NOT fine
            print "httplib.UNPROCESSABLE_ENTITY"
            content = json.loads(response.content)
            print content
        else:
            print statusCode
            print response

    def _update_entity(self, entityInstance):
        print "Update Entity"
        entity = Entity()
        entity.convertObjectToEntity(entityInstance)
        jsonString = JsonConvert.ToJSON(entity)
        jsonString = ContextBrokerHandler._remove_id_and_type(jsonString)
        print jsonString
        response = requests.patch(self._fiwareAddress + "/v2/entities/" + str(entity.id) + "/attrs", data=jsonString, headers=HEADERS)
        statusCode = response.status_code
        if isResponseOk(statusCode): # everything is fine
            entityInstance.clear_dirty()
            print "Status OK"
        elif statusCode == httplib.BAD_REQUEST: # everything is NOT fine
            print "httplib.UNPROCESSABLE_ENTITY"
            print statusCode
            print response
            print json.loads(response.content)
        else:
            print statusCode
            print response
            print json.loads(response.content)

    def _delete_entity(self, entity):
        #entity = Entity()
        #entity.convertObjectToEntity(entityInstance) 
        print "Delete Entity - Id: " + str (entity.id)
        response = requests.delete(self._fiwareAddress + "/v2/entities/" + str(entity.id))
        statusCode = response.status_code
        
        if(isResponseOk(statusCode)): # everything is fine
            print "Status OK"
            if entity in self._published_entities: # Not sure at all about this, probably shouldn't delete on creation and don't need that check
                self._published_entities.remove(entity)
            return 0
        else:
            content = json.loads(response.content)
            print content
            return statusCode

    @staticmethod
    def _remove_id_and_type(jsonString):
        jsonObject = json.loads(jsonString)
        del jsonObject["id"]
        del jsonObject["type"]
        return json.dumps(jsonObject, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    #endregion