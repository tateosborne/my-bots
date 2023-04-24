
import sys
from simulation import SIMULATION

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
isBest = sys.argv[3]
aOrB = sys.argv[4]
simulation = SIMULATION(directOrGUI, solutionID, isBest)
simulation.run(aOrB)
simulation.get_fitness()
