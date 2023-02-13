
import numpy
import matplotlib.pyplot
import constants as c

# leg sensors
# backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
# frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
# matplotlib.pyplot.plot(backLegSensorValues, label="back leg", linewidth=2)
# matplotlib.pyplot.plot(frontLegSensorValues, label="front leg", linewidth=2)
# matplotlib.pyplot.legend()
# matplotlib.pyplot.show()

# motor plot
targetAngles = numpy.load("data/targetAngles.npy")
matplotlib.pyplot.plot(numpy.arange(len(targetAngles)), targetAngles*c.PI/4)
matplotlib.pyplot.show()
