
from parallelhillclimber import PARALLEL_HILL_CLIMBER
import os


choice = input("new run or show best? (n / s): ")
if choice == "n":
    aOrB = input("test A or B (a / b): ")
    aOrB = aOrB.capitalize()
    phc = PARALLEL_HILL_CLIMBER("A" if aOrB=="A" else "B")
    phc.evolve()
    phc.show_best()
else:
    key = input("type key: ")
    aOrB = input("test A or B (a / b): ")
    aOrB = aOrB.capitalize()
    os.system(f"python3 simulate.py GUI {key} true {aOrB} 2&>1 &")
