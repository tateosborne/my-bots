
import copy
import constants as c
from solution import SOLUTION


class HILL_CLIMBER:
    
    def __init__(self):
        self.parent = SOLUTION()
        
        
    def evolve(self):
        self.parent.evaluate()
        for currentGeneration in range(c.NUMBER_OF_GENERATIONS):
            self.evolve_for_one_generation()
    
    def evolve_for_one_generation(self):
        self.spawn()
        self.mutate()
        self.child.evaluate()
        self.select()
        
    def spawn(self):
        self.child = copy.deepcopy(self.parent)
    
    def mutate(self):
        pass
    
    def select(self):
        pass
