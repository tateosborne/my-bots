
import os
import numpy
import pyrosim.pyrosim as pyrosim

class SOLUTION:
    
    def __init__(self):
        self.weights = numpy.random.rand(3, 2)
        self.weights = 2 * self.weights - 1
        
    
    def evaluate(self):
        self.create_world()
        self.generate_body()
        self.generate_brain()
        os.system("python3 simulate.py")
        fitnessFile = open("data/fitness.txt", "r")
        self.fitness = float(fitnessFile.read())
        fitnessFile.close()
    
    def create_world(self):    
        pyrosim.Start_SDF("world.sdf")

        pyrosim.Send_Cube(name="Box", pos=[-3.0,3,0.5] , size=[1,1,1])

        pyrosim.End()
    
    def generate_body(self):
        pyrosim.Start_URDF("body.urdf")
        
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1.5] , size=[1,1,1])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[-0.5,0,1.0])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5] , size=[1,1,1])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0.5,0,1.0])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[1,1,1])
        
        pyrosim.End()
        
    def generate_brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
        
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")
        
        for currentRow in range(0, 3):
            for currentColumn in range(0, 2):
                weight = self.weights[currentRow][currentColumn]
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+3, weight=weight)
        
        pyrosim.End()
    