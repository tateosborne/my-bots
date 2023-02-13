
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c
import time
import numpy


physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(c.GRAVITY_X, c.GRAVITY_Y, c.GRAVITY_Z)

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(c.LOOP_LENGTH)
frontLegSensorValues = numpy.zeros(c.LOOP_LENGTH)

backLegTargetAngles = numpy.zeros(c.LOOP_LENGTH)
frontLegTargetAngles = numpy.zeros(c.LOOP_LENGTH)

x = numpy.linspace(-c.PI, c.PI, c.LOOP_LENGTH)
backLegTargetAngles = c.AMPLITUDE_BACK * numpy.sin(c.FREQUENCY_BACK*x + c.PHASE_OFFSET_BACK)
frontLegTargetAngles = c.AMPLITUDE_FRONT * numpy.sin(c.FREQUENCY_FRONT*x + c.PHASE_OFFSET_FRONT)

# numpy.save("data/backLegTargetAngles.npy", backLegTargetAngles)
# numpy.save("data/frontLegTargetAngles.npy", frontLegTargetAngles)

# exit()

for i in range(c.LOOP_LENGTH):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId,
                                jointName="Torso_BackLeg",
                                controlMode=p.POSITION_CONTROL,
                                targetPosition=backLegTargetAngles[i],
                                maxForce=c.MOTOR_FORCE)
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId,
                                jointName="Torso_FrontLeg",
                                controlMode=p.POSITION_CONTROL,
                                targetPosition=frontLegTargetAngles[i],
                                maxForce=c.MOTOR_FORCE)
    
    time.sleep(c.SLEEP)

numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)

p.disconnect()
