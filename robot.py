
import pybullet as p
import os
import pyrosim.pyrosim as pyrosim
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK
from sensor import SENSOR
from motor import MOTOR


class ROBOT:

    def __init__(self, solutionID, isBest):
        self.sensors = {}
        self.motors = {}
        self.robotId = p.loadURDF("body.urdf")
        self.solutionID = solutionID
        self.prev_pos = p.getBasePositionAndOrientation(self.robotId)[0][2]
        if isBest == "true":
            self.nn = NEURAL_NETWORK(f"best_brain/brain{self.solutionID}.nndf")
        else:
            self.nn = NEURAL_NETWORK(f"brains/brain{self.solutionID}.nndf")
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
            
    def act(self, timeStep, aOrB):
        curr_pos = p.getBasePositionAndOrientation(self.robotId)[0][2]
        front_and_back = [9, 10, 11, 12] if aOrB == "A" else [5, 6, 7, 8]
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                
                if curr_pos < 0.4 or curr_pos > self.prev_pos:
                    if neuronName in front_and_back:
                        desiredAngle = self.nn.Get_Value_Of(neuronName) * c.MOTOR_JOINT_RANGE * -2
                    else:
                        desiredAngle = self.nn.Get_Value_Of(neuronName) * c.MOTOR_JOINT_RANGE * 2
                else:
                    if neuronName in front_and_back:
                        desiredAngle = self.nn.Get_Value_Of(neuronName) * c.MOTOR_JOINT_RANGE * -1
                    else:
                        desiredAngle = self.nn.Get_Value_Of(neuronName) * c.MOTOR_JOINT_RANGE * 1
                    
                self.motors[jointName].set_value(desiredAngle, self.robotId)
                    
        self.prev_pos = curr_pos
        # for neuronName in self.nn.Get_Neuron_Names():
        #     if self.nn.Is_Motor_Neuron(neuronName):
        #         jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
        #         desiredAngle = self.nn.Get_Value_Of(neuronName) * c.MOTOR_JOINT_RANGE
        #         for motor in self.motors:
        #             self.motors[motor].set_value(desiredAngle, self.robotId)

    def get_fitness(self):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        basePosition = basePositionAndOrientation[0]
        orientation = basePositionAndOrientation[1]
        zPosition = basePosition[2]
        xOrientation = abs(orientation[0])
        yOrientation = abs(orientation[1])
        zOrientation = abs(orientation[2])
        fitness = (1-xOrientation)*(1-yOrientation)*(1-zOrientation)*(zPosition)
        fitnessFile = open(f"tmp{self.solutionID}.txt", "w")
        os.system(f"mv tmp{self.solutionID}.txt fitness/fitness{self.solutionID}.txt")
        fitnessFile.write(str(fitness))
        fitnessFile.close()
        