
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c
import time
import numpy
import random
from math import pi


physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(c.GRAVITY_X, c.GRAVITY_Y, c.GRAVITY_Z)

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(c.LOOP_LENGTH)
frontLegSensorValues = numpy.zeros(c.LOOP_LENGTH)

targetAngles = numpy.zeros(c.LOOP_LENGTH)
x = numpy.linspace(-c.PI, c.PI, c.LOOP_LENGTH)
targetAngles = numpy.sin(x)
numpy.save("data/targetAngles.npy", targetAngles)

for i in range(c.LOOP_LENGTH):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId,
                                jointName="Torso_BackLeg",
                                controlMode=p.POSITION_CONTROL,
                                targetPosition=targetAngles[i],
                                maxForce=c.MOTOR_FORCE)
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId,
                                jointName="Torso_FrontLeg",
                                controlMode=p.POSITION_CONTROL,
                                targetPosition=targetAngles[i],
                                maxForce=c.MOTOR_FORCE)
    
    time.sleep(c.SLEEP)

numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)

p.disconnect()
