
import pybullet as p
import numpy
import pyrosim.pyrosim as pyrosim
import constants as c

class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        self.amplitude = c.AMPLITUDE_BACK
        self.frequency = c.FREQUENCY_BACK
        self.offset = c.PHASE_OFFSET_BACK
        self.force = c.MOTOR_FORCE
        self.prepare_to_act()
        
    
    def prepare_to_act(self):
        x = numpy.linspace(0, 2*c.PI, c.LOOP_LENGTH)
        self.motorValues =  self.amplitude * numpy.sin(self.frequency*x + self.offset)
        
    def set_value(self, timeStep, robotId):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.motorValues[timeStep],
            maxForce=self.force)