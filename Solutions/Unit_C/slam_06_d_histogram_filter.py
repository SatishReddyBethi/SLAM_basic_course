# Histogram implementation of a bayes filter - combines
# convolution and multiplication of distributions, for the
# movement and measurement steps.
# 06_d_histogram_filter
# Claus Brenner, 28 NOV 2012
import matplotlib.pyplot as plt
from distribution import *

def move(distribution, delta):
    """Returns a Distribution that has been moved (x-axis) by the amount of
       delta."""
    return Distribution(distribution.offset + delta, distribution.values)



# --->>> Copy your convolve(a, b) and multiply(a, b) functions here.
def convolve(a, b):
    """Convolve distribution a and b and return the resulting new distribution."""

    # --->>> Put your code here.
    final_values = []
    for i in range(len(a.values)):
        for j in range(len(b.values)):
            conv_value = a.values[i] * b.values[j]
            if (i+j+1)>len(final_values):
                final_values.append(conv_value)
            else:
                final_values[i+j] += conv_value
    
    return Distribution(a.offset + b.offset, final_values)

def multiply(a, b):
    """Multiply two distributions and return the resulting distribution."""

    # --->>> Put your code here.
    final_start = min([a.start(),b.start()])
    final_stop = max([a.stop(),b.stop()])
    final_values = []
    for i in range(final_start,final_stop):
        final_values.append(a.value(i)*b.value(i))

    final_dist = Distribution(final_start, final_values)
    final_dist.normalize()
    return final_dist


if __name__ == '__main__':
    arena = (0,220)

    # Start position. Exactly known - a unit pulse.
    start_position = 10
    position = Distribution.unit_pulse(start_position)
    plt.plot(position.plotlists(*arena)[0], position.plotlists(*arena)[1],
         drawstyle='steps')

    # Movement data.
    controls  =    [ 20 ] * 10

    # Measurement data. Assume (for now) that the measurement data
    # is correct. - This code just builds a cumulative list of the controls,
    # plus the start position.
    p = start_position
    measurements = []
    for c in controls:
        p += c
        measurements.append(p)

    # This is the filter loop.
    for i in range(len(controls)):
        # Move, by convolution. Also termed "prediction".
        control = Distribution.triangle(controls[i], 10)
        position = convolve(position, control)
        plt.plot(position.plotlists(*arena)[0], position.plotlists(*arena)[1],
             color='b', drawstyle='steps')

        # Measure, by multiplication. Also termed "correction".
        measurement = Distribution.triangle(measurements[i], 10)
        position = multiply(position, measurement)
        plt.plot(position.plotlists(*arena)[0], position.plotlists(*arena)[1],
             color='r', drawstyle='steps')

    plt.show()
