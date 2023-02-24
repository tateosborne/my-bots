
import pybullet as p
import numpy
import pyrosim.pyrosim as pyrosim
import constants as c

class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        self.amplitude = c.AMPLITUDE
        self.frequency = c.FREQUENCY
        self.offset = c.PHASE_OFFSET
        self.force = c.MOTOR_FORCE
        self.motorValues = numpy.zeros(c.LOOP_LENGTH)
        
        
    def set_value(self, desiredAngle, robotId):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=desiredAngle,
            maxForce=self.force)
        