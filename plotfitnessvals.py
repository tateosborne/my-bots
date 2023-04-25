
import numpy
import matplotlib.pyplot as plt
import constants as c


testA = numpy.load(f"matrices/matrixA.npy")
testB = numpy.load(f"matrices/matrixB.npy")

avgA = numpy.mean(testA, axis=1)
avgB = numpy.mean(testB, axis=1)

stdA = numpy.std(avgA)
stdB = numpy.std(avgB)
    
plt.plot(avgA, label="Test A (four legs)", linewidth=3, color="red")
plt.plot(avgA+stdA, linestyle="dotted", linewidth=3, color="orange")
plt.plot(avgA-stdA, linestyle="dotted", linewidth=3, color="orange")

plt.plot(avgB, label="Test B (two legs)", linewidth=3, color="purple")
plt.plot(avgB+stdB, linestyle="dotted", linewidth=3, color="pink")
plt.plot(avgB-stdB, linestyle="dotted", linewidth=3, color="pink")

plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

plt.title("Fitness Over Time")
plt.xlabel("Generation")
plt.ylabel("Fitness")

plt.legend()
plt.show()
