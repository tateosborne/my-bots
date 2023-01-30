
import pyrosim.pyrosim as pyrosim


def create_world():    
    pyrosim.Start_SDF("world.sdf")

    # pyrosim.Send_Cube(name="Box", pos=[-2.0,2,0.5] , size=[1,1,1])

    pyrosim.End()
    
def create_robot():
    pyrosim.Start_URDF("body.urdf")
    
    pyrosim.Send_Cube(name="Link0", pos=[0,0,0.5] , size=[1,1,1])
    
    pyrosim.Send_Joint(name="Link0_Link1", parent="Link0", child="Link1", type="revolute", position=[0.5,0,1.0])
    
    pyrosim.Send_Cube(name="Link1", pos=[0.5,0,0.5] , size=[1,1,1])
    
    pyrosim.End()

create_world()
create_robot()