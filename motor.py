
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
        self.prepare_to_act()
        
    
    def prepare_to_act(self):
        x = numpy.linspace(0, 2*c.PI, c.LOOP_LENGTH)
        
        if self.jointName == "Torso_BackLeg":
            self.motorValues = numpy.sin((self.frequency/2)*x + self.offset) * self.amplitude
        else:
            self.motorValues = numpy.sin(self.frequency*x + self.offset) * self.amplitude
        
    def set_value(self, desiredAngle, robotId):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=desiredAngle,
            maxForce=self.force)
        
    def save_motor_values(self):
         numpy.save("data/motorValues.npy", self.motorValues)
    