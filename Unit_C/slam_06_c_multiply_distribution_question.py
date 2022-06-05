# Multiply a distribution by another distribution.
# 06_c_multiply_distribution
# Claus Brenner, 26 NOV 2012
import matplotlib.pyplot as plt
from distribution import *

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
     return final_dist # Modify this to return your result.


if __name__ == '__main__':
     arena = (0,1000)

     # Here is our assumed position. Plotted in blue.
     position_value = 400
     position_error = 100
     position = Distribution.triangle(position_value, position_error)
     plt.plot(position.plotlists(*arena)[0], position.plotlists(*arena)[1],
          color='b', drawstyle='steps')

     # Here is our measurement. Plotted in green.
     # That is what we read from the instrument.
     measured_value = 410
     measurement_error = 200
     measurement = Distribution.triangle(measured_value, measurement_error)
     plt.plot(measurement.plotlists(*arena)[0], measurement.plotlists(*arena)[1],
          color='g', drawstyle='steps')

     # Now, we integrate our sensor measurement. Result is plotted in red.
     position_after_measurement = multiply(position, measurement)
     plt.plot(position_after_measurement.plotlists(*arena)[0],
          position_after_measurement.plotlists(*arena)[1],
          color='r', drawstyle='steps')

     plt.show()
