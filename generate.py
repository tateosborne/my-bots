
import pyrosim.pyrosim as pyrosim


def create_world():    
    pyrosim.Start_SDF("world.sdf")

    pyrosim.Send_Cube(name="Box", pos=[-2,2,0.5] , size=[1,1,1])

    pyrosim.End()
    
def create_robot():
    pyrosim.Start_URDF("body.urdf")
    
    pyrosim.Send_Cube(name="Torso", pos=[0,0,0.5] , size=[1,1,1])
    
    pyrosim.End()

create_world()
create_robot()