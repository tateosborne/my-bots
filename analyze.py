
import numpy
import matplotlib.pyplot


backLegSensorValues = numpy.load("data/back-leg-sensor-values.npy")

# print(backLegSensorValues)

matplotlib.pyplot.plot(backLegSensorValues)
matplotlib.pyplot.show()
