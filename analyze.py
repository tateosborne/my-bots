
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

# target angles for motors
backLegTargetAngles = numpy.load("data/backLegTargetAngles.npy")
frontLegTargetAngles = numpy.load("data/frontLegTargetAngles.npy")
matplotlib.pyplot.plot(numpy.arange(len(backLegTargetAngles)), backLegTargetAngles, label="back leg motor values", linewidth=2)
matplotlib.pyplot.plot(numpy.arange(len(frontLegTargetAngles)), frontLegTargetAngles, label = "front leg motor values", linewidth=2)
matplotlib.pyplot.xlabel('Steps')
matplotlib.pyplot.ylabel('Value in Radians')
matplotlib.pyplot. legend ( )
matplotlib.pyplot.show()
