
import os
import copy
import constants as c
from solution import SOLUTION


class PARALLEL_HILL_CLIMBER:
    
    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.POP_SIZE):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1
        
        
    def evolve(self):
        for key in self.parents:
            self.parents[key].start_simulation("DIRECT")
            for currentGeneration in range(c.NUMBER_OF_GENERATIONS):
                self.evolve_for_one_generation()
        for key in self.parents:
            self.parents[key].wait_for_simulation_to_end()
    
    def evolve_for_one_generation(self):
        self.spawn()
        self.mutate()
        # self.child.evaluate("DIRECT")
        # self.print_fitness()
        # self.select()
        
    def spawn(self):
        self.children = {}
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].set_id(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1
    
    def mutate(self):
        for key in self.children:
            self.children[key].mutate()
    
    def select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child
            
    def print_fitness(self):
        print(f"\n\nparent fitness: {self.parent.fitness} || child fitness: {self.child.fitness}\n")
        
    def show_best(self):
        # self.parent.evaluate("GUI")
        pass
