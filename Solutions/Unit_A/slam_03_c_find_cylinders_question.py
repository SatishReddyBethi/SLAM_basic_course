# For each cylinder in the scan, find its ray and depth.
# 03_c_find_cylinders
# Claus Brenner, 09 NOV 2012
import matplotlib.pyplot as plt
from lego_robot import *

# Find the derivative in scan data, ignoring invalid measurements.
def compute_derivative(scan, min_dist):
    jumps = [ 0 ]
    for i in range(1, len(scan) - 1):
        l = scan[i-1]
        r = scan[i+1]
        if l > min_dist and r > min_dist:
            derivative = (r - l) / 2.0
            jumps.append(derivative)
        else:
            jumps.append(0)
    jumps.append(0)
    return jumps

# For each area between a left falling edge and a right rising edge,
# determine the average ray number and the average depth.
def find_cylinders(scan, scan_derivative, jump, min_dist):
    cylinder_list = []
    sum_ray, sum_depth, ray_count = 0.0, 0.0, 0
    cylinder_start = False
    cylinder_end = False
    start_list = []
    end_list = []

    for i in range(len(scan_derivative)):
        # --->>> Insert your cylinder code here.
        # Whenever you find a cylinder, add a tuple
        # (average_ray, average_depth) to the cylinder_list.

        # Just for fun, I'll output some cylinders.
        # Replace this by your code.
        if(scan_derivative[i] < -jump):
            cylinder_start = True
            cylinder_end = False
            sum_ray = 0
            ray_count = 0
            sum_depth = 0
            start_list.append(i)

        if(scan_derivative[i] > jump):
            cylinder_end = True
            end_list.append(i)

        if(cylinder_start):
            sum_ray += i
            sum_depth += scan[i]
            ray_count += 1

        if(cylinder_end and ray_count > 0):
            cylinder_start = False
            cylinder_end = False
            avg_ray = sum_ray/ray_count
            avg_depth = sum_depth/ray_count
            sum_ray = 0
            ray_count = 0
            sum_depth = 0
            cylinder_list.append( (avg_ray, avg_depth) )

    return cylinder_list


if __name__ == '__main__':

    minimum_valid_distance = 20.0
    depth_jump = 100.0

    # Read the logfile which contains all scans.
    logfile = LegoLogfile()
    logfile.read("robot4_scan.txt")

    # Pick one scan.
    scan = logfile.scan_data[8]

    # Find cylinders.
    der = compute_derivative(scan, minimum_valid_distance)
    cylinders = find_cylinders(scan, der, depth_jump,
                               minimum_valid_distance)

    # Plot results.
    plt.plot(scan)
    plt.scatter([c[0] for c in cylinders], [c[1] for c in cylinders], c='r', s=200)
    plt.show()
