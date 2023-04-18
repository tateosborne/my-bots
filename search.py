
from parallelhillclimber import PARALLEL_HILL_CLIMBER
import os


choice = input("new run or show best? (nr / sb): ")
if choice == "nr":
    phc = PARALLEL_HILL_CLIMBER()
    phc.evolve()
    phc.show_best()
else:
    key = input("type key: ")
    os.system(f"python3 simulate.py GUI {key} true 2&>1 &")
