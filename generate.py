
import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

x = 0
y = 0
z = 0.5

length = 1
width = 1
height = 1

for i in range(5):
    for j in range(5):
        for k in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x+i, y+j, z+k] , size=[length*(1-k/10), width*(1-k/10), height*(1-k/10)])

pyrosim.End()
