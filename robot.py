
import pybullet as p
import os
import pyrosim.pyrosim as pyrosim
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK
from sensor import SENSOR
from motor import MOTOR


class ROBOT:

    def __init__(self, solutionID):
        self.sensors = {}
        self.motors = {}
        self.robotId = p.loadURDF("body.urdf")
        self.solutionID = solutionID
        self.nn = NEURAL_NETWORK(f"brain{self.solutionID}.nndf")
        os.system(f"rm brain{solutionID}.nndf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.prepare_to_sense()
        self.prepare_to_act()
    
    
    def prepare_to_sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
            
    def sense(self, timeStep):
        for sensor in self.sensors:
            self.sensors[sensor].get_value(timeStep)
            
    def think(self, timeStep):
        self.nn.Update()
            
    def prepare_to_act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
            
    def act(self, timeStep):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.MOTOR_JOINT_RANGE
                for motor in self.motors:
                    self.motors[motor].set_value(desiredAngle, self.robotId)
                    
    def get_fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId,0)
        linkPosition = stateOfLinkZero[0]
        xPosition = linkPosition[0]
        fitnessFile = open(f"tmp{self.solutionID}.txt", "w")
        os.system(f"mv tmp{self.solutionID}.txt fitness{self.solutionID}.txt")
        fitnessFile.write(xPosition)
        fitnessFile.close()
        