
import sys
from simulation import SIMULATION

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
isBest = sys.argv[3]
simulation = SIMULATION(directOrGUI, solutionID, isBest)
simulation.run()
simulation.get_fitness()
