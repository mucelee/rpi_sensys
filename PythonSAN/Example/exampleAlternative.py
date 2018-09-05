import time
import threading

from exampleSensorAlternative import ExampleSensorAlternative

sensor = ExampleSensorAlternative()

def loop():
    i = 0
    while True:
        i += 1
        sensor.addReading(i)
        sensor.set_dirty()
        time.sleep(1)

def startLoop():
    threading.Thread(target=loop).start()