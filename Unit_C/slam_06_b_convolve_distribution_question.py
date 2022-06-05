# Instead of moving a distribution, move (and modify) it using a convolution.
# 06_b_convolve_distribution
# Claus Brenner, 26 NOV 2012
from distribution import *
import matplotlib.pyplot as plt

def move(distribution, delta):
    """Returns a Distribution that has been moved (x-axis) by the amount of
       delta."""
    return Distribution(distribution.offset + delta, distribution.values)

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
    
    return Distribution(a.offset + b.offset, final_values)  # Replace this by your own result.


if __name__ == '__main__':
    arena = (0,100)

    # Move 3 times by 20.
    moves = [20] * 3

    # Start with a known position: probability 1.0 at position 10.
    position = Distribution.unit_pulse(10)
    plt.plot(position.plotlists(*arena)[0], position.plotlists(*arena)[1],
         drawstyle='steps')

    # Now move and plot.
    for m in moves:
        move_distribution = Distribution.triangle(m, 2)
        position = convolve(position, move_distribution)
        plt.plot(position.plotlists(*arena)[0], position.plotlists(*arena)[1],
             drawstyle='steps')

    plt.ylim(0.0, 1.1)
    plt.show()
