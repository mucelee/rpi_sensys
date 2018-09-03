import time;

from baseFiwareClass import BaseFiwareClass;

from taskId import TaskId;

def enum(**enums):
        return type('Enum', (), enums)

TaskStatus  = enum(Init=0, Running = 1, Waiting = 2,  WaitingOrAborting = 3, Active = 4, Finished = 5, Aborted = 6, Error = 7)


class TaskMonitoring(BaseFiwareClass):
    """description of class"""
    
    def __init__(self):
        self.currentTaskState = TaskStatus.Init
        self.time = time.time()
        self.estimatedEndTimeTask = -1  
        self.timeout = 1000;
        self.taskId = TaskId()
    
    def __repr__(self):
        retVal = ""
        retVal = "Type: " + str(self.__class__.__name__)
        return retVal

    