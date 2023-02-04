
import numpy
import matplotlib.pyplot


backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")

# print(backLegSensorValues)

matplotlib.pyplot.plot(backLegSensorValues, label="back leg", linewidth=2)
matplotlib.pyplot.plot(frontLegSensorValues, label="front leg", linewidth=2)

matplotlib.pyplot.legend()
matplotlib.pyplot.show()
