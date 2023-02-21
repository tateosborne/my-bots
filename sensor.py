
import pyrosim.pyrosim as pyrosim
import numpy

import constants as c


class SENSOR:

    def __init__(self, linkName):
        self.linkName = linkName
        self.sensorValues = numpy.zeros(c.LOOP_LENGTH)
        
    
    def get_value(self, timeStep):
        self.sensorValues[timeStep] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        
    def save_sensor_values(self):
        numpy.save("data/sensorValues.npy", self.sensorValues)
        