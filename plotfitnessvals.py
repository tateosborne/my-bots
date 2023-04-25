
import numpy
import matplotlib.pyplot as plt
import constants as c


arrayAvgA = []
arrayAvgB = []
arrayStdA = []
arrayStdB = []

for i in range(10):
    testA = numpy.load(f"matrices/matrixA_{i}.npy")
    testB = numpy.load(f"matrices/matrixB_{i}.npy")

    avgA = numpy.mean(testA, axis=1)
    arrayAvgA.append(avgA)
    avgB = numpy.mean(testB, axis=1)
    arrayAvgB.append(avgB)
    
    stdA = numpy.std(avgA)
    arrayStdA.append(stdA)
    stdB = numpy.std(avgB)
    arrayStdB.append(stdB)
    
avgA = numpy.mean(arrayAvgA, axis=0)
avgB = numpy.mean(arrayAvgB, axis=0)
stdA = numpy.mean(arrayStdA, axis=0)
stdB = numpy.mean(arrayStdB, axis=0)
    
plt.plot(avgA, label="Test A (four legs)", linewidth=3, color="red")
plt.plot(avgA+stdA, linestyle="dotted", linewidth=3, color="red")
plt.plot(avgA-stdA, linestyle="dotted", linewidth=3, color="red")

plt.plot(avgB, label="Test B (two legs)", linewidth=3, color="purple")
plt.plot(avgB+stdB, linestyle="dotted", linewidth=3, color="purple")
plt.plot(avgB-stdB, linestyle="dotted", linewidth=3, color="purple")

plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

plt.title("Fitness Over Time")
plt.xlabel("Generation")
plt.ylabel("Fitness")

plt.legend()
plt.show()
