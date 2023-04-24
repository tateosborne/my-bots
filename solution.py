
import os
import time
import numpy
import random
import pyrosim.pyrosim as pyrosim
import constants as c

class SOLUTION:
    
    def __init__(self, myID, aOrB):
        self.weights = numpy.random.rand(c.NUM_SENSOR_NEURONS_A if aOrB=="A" else c.NUM_SENSOR_NEURONS_B, c.NUM_MOTOR_NEURONS_A if aOrB=="A" else c.NUM_MOTOR_NEURONS_B)
        self.weights = 2 * self.weights - 1
        self.myID = myID
        self.aOrB = aOrB
        
    
    def start_simulation(self, directOrGUI, aOrB):
        self.create_world()
        self.generate_body(aOrB)
        self.generate_brain(aOrB)
        os.system(f"python3 simulate.py {directOrGUI} {self.myID} false {aOrB} 2&>1 &")
    
    def wait_for_simulation_to_end(self):
        while not os.path.exists(f"fitness/fitness{self.myID}.txt"):
            time.sleep(0.1)
        fitnessFile = open(f"fitness/fitness{self.myID}.txt", "r")
        self.fitness = fitnessFile.read()
        while self.fitness == "":
            time.sleep(0.1)
            self.fitness = fitnessFile.read()
        self.fitness = float(self.fitness)
        fitnessFile.close()
        os.system(f"rm fitness/fitness{self.myID}.txt")
        
    def mutate(self):
        randomRow = random.randint(0, c.NUM_SENSOR_NEURONS_A-1 if self.aOrB=="A" else c.NUM_SENSOR_NEURONS_B-1)
        randomColumn = random.randint(0, c.NUM_MOTOR_NEURONS_A-1 if self.aOrB=="A" else c.NUM_MOTOR_NEURONS_B-1)
        self.weights[randomRow,randomColumn] = (2 * random.random() - 1)
    
    def create_world(self):    
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()
    
    def generate_body(self, aOrB):
        if aOrB == "A":
            pyrosim.Start_URDF("body.urdf")
            pyrosim.Send_Cube(name="Torso", pos=[0,0,2] , size=[1,1,1])
            
            pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0,-0.5,2], jointAxis = "1 0 0")
            pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0] , size=[0.25,1,0.25])
            pyrosim.Send_Joint(name="BackLeg_LowerBackLeg", parent="BackLeg", child="LowerBackLeg", type="revolute", position=[0,-1,0], jointAxis = "1 0 0")
            pyrosim.Send_Cube(name="LowerBackLeg", pos=[0,0,-0.5] , size=[0.25,0.25,1])
            
            pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0,0.5,2], jointAxis = "1 0 0")
            pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0] , size=[0.25,1,0.25])
            pyrosim.Send_Joint(name="FrontLeg_LowerFrontLeg", parent="FrontLeg", child="LowerFrontLeg", type="revolute", position=[0,1,0], jointAxis = "1 0 0")
            pyrosim.Send_Cube(name="LowerFrontLeg", pos=[0,0,-0.5] , size=[0.25,0.25,1])
            
            pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute", position=[-0.5,0,2], jointAxis = "0 1 0")
            pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5,0,0] , size=[1,0.25,0.25])
            pyrosim.Send_Joint(name="LeftLeg_LowerLeftLeg", parent="LeftLeg", child="LowerLeftLeg", type="revolute", position=[-1,0,0], jointAxis = "0 1 0")
            pyrosim.Send_Cube(name="LowerLeftLeg", pos=[0,0,-0.5] , size=[0.25,0.25,1])
            
            pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute", position=[0.5,0,2], jointAxis = "0 1 0")
            pyrosim.Send_Cube(name="RightLeg", pos=[0.5,0,0] , size=[1,0.25,0.25])
            pyrosim.Send_Joint(name="RightLeg_LowerRightLeg", parent="RightLeg", child="LowerRightLeg", type="revolute", position=[1,0,0], jointAxis = "0 1 0")
            pyrosim.Send_Cube(name="LowerRightLeg", pos=[0,0,-0.5] , size=[0.25,0.25,1])
            
            pyrosim.End() 
            
        else:
            pyrosim.Start_URDF("body.urdf")
            pyrosim.Send_Cube(name="Torso", pos=[0,0,2] , size=[1,1,1])
            
            pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0,-0.5,2], jointAxis = "1 0 0")
            pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0] , size=[0.5,1,0.2])
            pyrosim.Send_Joint(name="BackLeg_LowerBackLeg", parent="BackLeg", child="LowerBackLeg", type="revolute", position=[0,-1,0], jointAxis = "1 0 0")
            pyrosim.Send_Cube(name="LowerBackLeg", pos=[0,0,-0.5] , size=[0.5,0.2,1])
            
            pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0,0.5,2], jointAxis = "1 0 0")
            pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0] , size=[0.5,1,0.2])
            pyrosim.Send_Joint(name="FrontLeg_LowerFrontLeg", parent="FrontLeg", child="LowerFrontLeg", type="revolute", position=[0,1,0], jointAxis = "1 0 0")
            pyrosim.Send_Cube(name="LowerFrontLeg", pos=[0,0,-0.5] , size=[0.5,0.2,1])
            
            pyrosim.End()
        
    def generate_brain(self, aOrB):
        if aOrB == "A":
            pyrosim.Start_NeuralNetwork(f"brains/brain{self.myID}.nndf")
            pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
            pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
            pyrosim.Send_Sensor_Neuron(name=2, linkName="LowerBackLeg")
            pyrosim.Send_Sensor_Neuron(name=3, linkName="FrontLeg")
            pyrosim.Send_Sensor_Neuron(name=4, linkName="LowerFrontLeg")
            pyrosim.Send_Sensor_Neuron(name=5, linkName="LeftLeg")
            pyrosim.Send_Sensor_Neuron(name=6, linkName="LowerLeftLeg")
            pyrosim.Send_Sensor_Neuron(name=7, linkName="RightLeg")
            pyrosim.Send_Sensor_Neuron(name=8, linkName="LowerRightLeg")
            pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_BackLeg")
            pyrosim.Send_Motor_Neuron(name=10, jointName="BackLeg_LowerBackLeg")
            pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_FrontLeg")
            pyrosim.Send_Motor_Neuron(name=12, jointName="FrontLeg_LowerFrontLeg")
            pyrosim.Send_Motor_Neuron(name=13, jointName="Torso_LeftLeg")
            pyrosim.Send_Motor_Neuron(name=14, jointName="LeftLeg_LowerLeftLeg")
            pyrosim.Send_Motor_Neuron(name=15, jointName="Torso_RightLeg")
            pyrosim.Send_Motor_Neuron(name=16, jointName="RightLeg_LowerRightLeg")
        
            for currentRow in range(0, c.NUM_SENSOR_NEURONS_A):
                for currentColumn in range(0, c.NUM_MOTOR_NEURONS_A):
                    weight = self.weights[currentRow][currentColumn]
                    pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+c.NUM_SENSOR_NEURONS_A, weight=weight)
                    
            pyrosim.End()
                    
        else:
            pyrosim.Start_NeuralNetwork(f"brains/brain{self.myID}.nndf")
            pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
            pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
            pyrosim.Send_Sensor_Neuron(name=2, linkName="LowerBackLeg")
            pyrosim.Send_Sensor_Neuron(name=3, linkName="FrontLeg")
            pyrosim.Send_Sensor_Neuron(name=4, linkName="LowerFrontLeg")
            pyrosim.Send_Motor_Neuron(name=5, jointName="Torso_BackLeg")
            pyrosim.Send_Motor_Neuron(name=6, jointName="BackLeg_LowerBackLeg")
            pyrosim.Send_Motor_Neuron(name=7, jointName="Torso_FrontLeg")
            pyrosim.Send_Motor_Neuron(name=8, jointName="FrontLeg_LowerFrontLeg")
            
            for currentRow in range(0, c.NUM_SENSOR_NEURONS_B):
                for currentColumn in range(0, c.NUM_MOTOR_NEURONS_B):
                    weight = self.weights[currentRow][currentColumn]
                    pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+c.NUM_SENSOR_NEURONS_B, weight=weight)
            
            pyrosim.End()
        
    def set_id(self, newID):
        self.myID = newID
    