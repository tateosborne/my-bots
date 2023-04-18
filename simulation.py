
import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import constants as c
from world import WORLD
from robot import ROBOT


class SIMULATION:

    def __init__(self, directOrGUI, solutionID, isBest):
        self.directOrGUI = directOrGUI
        if self.directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(c.GRAVITY_X, c.GRAVITY_Y, c.GRAVITY_Z)
        
        self.world = WORLD()
        self.robot = ROBOT(solutionID, isBest)
        
        
    def run(self):
        for t in range(c.LOOP_LENGTH):
            p.stepSimulation()
            
            self.robot.sense(t)
            self.robot.think(t)
            self.robot.act(t)
            
            if self.directOrGUI == "GUI":
                time.sleep(c.SLEEP)
            
    def get_fitness(self):
        self.robot.get_fitness()
            
    
    def __del__(self):
        p.disconnect()
