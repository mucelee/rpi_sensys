class Task(object):
    """description of class"""
    def __init__(self):
        self.task = ""
        self.ENTITY_TYPE = "TaskSpec"
        self.ENTITY_ID = "TaskSpecification_V_01"
        self.ENTITY_ATTR_NOTIFY = 'task", "erp'
        self.MIN_INTERVAL = "PT1S"
        self.DURATION = "PT1H"
        self.SERVER_URL = "http://10.64.2.70:5555/mod.sw.tp/task"
