
import os
import copy
import math
import constants as c
from solution import SOLUTION


class PARALLEL_HILL_CLIMBER:
    
    def __init__(self):
        os.system("rm brains/brain*.nndf")
        os.system("rm fitness/fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.POP_SIZE):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1
        
        
    def evolve(self):
        self.evaluate(self.parents)
        for currentGeneration in range(c.NUMBER_OF_GENERATIONS):
            print()
            print(f"generation {currentGeneration}")
            self.evolve_for_one_generation()
        
    def evaluate(self, solutions):
        for key in solutions:
            solutions[key].start_simulation("DIRECT")
        for key in solutions:
            solutions[key].wait_for_simulation_to_end()

    def evolve_for_one_generation(self):
        self.spawn()
        self.mutate()
        self.evaluate(self.children)
        self.print_fitness()
        self.select()
        
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
        for key in self.parents:
            if self.parents[key].fitness < self.children[key].fitness:
                self.parents[key] = self.children[key]
            
    def print_fitness(self):
        for key in self.parents:
            print(f"parent {key} fitness: {round(self.parents[key].fitness, 6)}\t\tchild fitness: {round(self.children[key].fitness, 6)}")
        
    def show_best(self):
        curr_best = 0
        best_key = -1
        for key in range(c.POP_SIZE):
            if self.parents[key].fitness > curr_best:
                curr_best = self.parents[key].fitness
                best_key = key
        
        os.system("rm best_brain/brain*.nndf")
        os.system(f"mv brains/brain{(c.POP_SIZE*c.NUMBER_OF_GENERATIONS) - c.POP_SIZE + best_key}.nndf best_brain/brain{(c.POP_SIZE*c.NUMBER_OF_GENERATIONS) - c.POP_SIZE + best_key}.nndf")
        os.system(f"rm brains/brain*.nndf")
        print(f"\n\nshowing parent {best_key} with its fitness of {self.parents[best_key].fitness}\n")
        self.parents[best_key].start_simulation("GUI")
        