
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import numpy
import random
from math import pi


physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName="Torso_BackLeg", controlMode=p.POSITION_CONTROL, targetPosition=-pi/4.0, maxForce=500)
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName="Torso_FrontLeg", controlMode=p.POSITION_CONTROL, targetPosition=pi/4.0, maxForce=500)
    
    time.sleep(1/60)

numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)

p.disconnect()
