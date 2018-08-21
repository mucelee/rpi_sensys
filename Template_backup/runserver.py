"""
This script runs the Template application using a development server.
"""

from os import environ
from Template import app
import time

import urllib2
import threading
from threading import Event, Thread
from Template.configParser import Config
from flask import g 

# local imports
from Template.mod.sw.task import Task 

from Template.Fiware.contextBrokerHandler import ContextBrokerHandler
from Template.Fiware.entitiyObserver import EntityAttributeChangeObserver

from Template.mod.sw.taskMonitoring import TaskMonitoring

HOST = '0.0.0.0'
PORT = 5555
SERVER_ADDRESS = "localhost"

CONFIG_FILE = "fiware_config.ini"
parsedConfigFile = Config(CONFIG_FILE)
 
          

def flaskThread():
    app.run(host= "0.0.0.0", port= PORT, threaded=True,use_reloader=False, debug = False)
    
def checkServerRunning(e):
    doForever = True
    
    while doForever:
        print "checkServerRunning"
         
        try:
            request = urllib2.Request("http://"+ SERVER_ADDRESS+  ":" + str(PORT) ) 
            response = urllib2.urlopen(request)        
            e.set()   
            print "set item"
            doForever = False
        except urllib2.HTTPError, err:
            print('HTTPError = ' + str(err.code))
        except urllib2.URLError, err:
            print('URLError = ' + str(err.reason))
            
        except httplib.HTTPException, err:
            print('HTTPException')
        else:
            print "FAILED"
            #doForever = False
            #e.set()
            #print response.read()


if __name__ == '__main__': 
    eventThreadSynchronizer = threading.Event()
    
    checkIfServerIsUpRunning = threading.Thread(name='checkServerRunning', 
                                                target=checkServerRunning, 
                                                args=(eventThreadSynchronizer,))

    flaskServerThread = threading.Thread(name= 'flaskThread',target = flaskThread) 

    checkIfServerIsUpRunning.start()        
    flaskServerThread.start()

    # create an instance of the fiware ocb handler
    ocbHandler = ContextBrokerHandler(parsedConfigFile.getFiwareServerAddress())


    entityAttributeChangePublisher = EntityAttributeChangeObserver(parsedConfigFile.getFiwareServerAddress())

    taskMon = TaskMonitoring()
     
    # before registering/publishing the entities, attaching is required
    ocbHandler.attach_entity(taskMon)
    # after adding it to the ocbHandler, feel free to register/publish the entities
    ocbHandler.register_entities();
    
    taskMon.attach_publisher(entityAttributeChangePublisher);
    
    taskMon.time = "23";
    # wait until server is available
    while not eventThreadSynchronizer.isSet():
        pass
    print "Done"
    user_input = ""
    while user_input!= "exit":
        user_input = raw_input("-->")
    
        
    ocbHandler.unregister_entities()
    #SubscribtionHandler.unsubscribeContext(parsedConfigFile)
    print "shutdown flask"    
