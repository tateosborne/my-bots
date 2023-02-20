
import pybullet as p
import pyrosim.pyrosim as pyrosim

from sensor import SENSOR
from motor import MOTOR


class ROBOT:

    def __init__(self):
        self.sensor = {}
        self.motor = {}
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate()
    