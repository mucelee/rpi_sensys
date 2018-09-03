import datetime

class SensorReading(object):

    _metadata_modifiedTime = {"timeFormat": "ISO8601"}

    def __init__(self, readingValue):
        self.reading = readingValue
        self.modifiedTime = datetime.datetime.now().isoformat()