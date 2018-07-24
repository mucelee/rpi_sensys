#!/usr/bin/env python
import ads1256
import time
import math

# configuration #
adcChannel = 2
publishInterval = 1
readFrequency = 30000 # ADC's SPS parameter. Possible values:   2d5,  5,  10,  15,  25,  30,  50,  60,  100,  500,  1000,  2000,  3750,  7500,  15000,  30000
smoothingFactor = 0.01
#################

voltageAverage = 0
voltagePositiveAverage = 0
nextPublishTime = 0
ads1256.start("1",str(readFrequency))

def Loop(channelValue):
        global voltageAverage, voltagePositiveAverage, nextPublishTime
        voltage = ((channelValue*100)/167.0)/1000000.0
        if(voltageAverage == 0):
                voltageAverage = voltage
                voltagePositiveAverage = voltage
        else:
                voltageAverage = voltage * smoothingFactor + voltageAverage * (1 - smoothingFactor)
                if(voltage > voltageAverage):
                        voltagePositiveAverage = voltage * smoothingFactor + voltagePositiveAverage * (1 - smoothingFactor)
        currentTime = time.clock()
        if(currentTime < nextPublishTime):
                return
        
        nextPublishTime = currentTime + publishInterval
        rmsMillivolts = math.floor((voltagePositiveAverage - voltageAverage) * 1000)
        print(rmsMillivolts)

def ReadValues():
        while True:
                Loop(ads1256.read_channel(adcChannel))
                time.sleep(1 / readFrequency / 2)
        ads1256.stop()
        
ReadValues()

ads1256.stop()
