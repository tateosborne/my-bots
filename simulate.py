
import sys
from simulation import SIMULATION

directOrGUI = sys.argv[1]
simulation = SIMULATION(directOrGUI)
simulation.run()
simulation.get_fitness()
