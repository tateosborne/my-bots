
import copy
import constants as c
from solution import SOLUTION


class PARALLEL_HILL_CLIMBER:
    
    def __init__(self):
        self.parents = {}
        for i in range(c.POP_SIZE):
            self.parents[i] = SOLUTION()
        
        
    def evolve(self):
        for key in self.parents:
            self.parents[key].evaluate("GUI")
            # for currentGeneration in range(c.NUMBER_OF_GENERATIONS):
            #     self.evolve_for_one_generation()
    
    def evolve_for_one_generation(self):
        self.spawn()
        self.mutate()
        self.child.evaluate("DIRECT")
        self.print_fitness()
        self.select()
        
    def spawn(self):
        self.child = copy.deepcopy(self.parent)
    
    def mutate(self):
        self.child.mutate()
    
    def select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child
            
    def print_fitness(self):
        print(f"\n\nparent fitness: {self.parent.fitness} || child fitness: {self.child.fitness}\n")
        
    def show_best(self):
        # self.parent.evaluate("GUI")
        pass
