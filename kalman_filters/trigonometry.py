# Python's math module has functions called sin, cos, and tan
# as well as the constant "pi" (which we will find useful shortly)
from math import sin, cos, tan, pi

# Run this cell. What do you expect the output to be?
print(sin(60))


from math import pi
def deg2rad(theta):
    """Converts degrees to radians"""
    # TODO - implement this function (solution
    #    code at end of notebook)
    return theta * pi / 180

assert(deg2rad(45.0) == pi / 4)
assert(deg2rad(90.0) == pi / 2)
print("Nice work! Your degrees to radians function works!")

for theta in [0, 30, 45, 60, 90]:
    theta_rad = deg2rad(theta)
    sin_theta = sin(theta_rad)
    print("sin(", theta, "degrees) =", sin_theta)




import numpy as np
from matplotlib import pyplot as plt
def plot_sine(min_theta, max_theta):
    """
    Generates a plot of sin(theta) between min_theta
    and max_theta (both of which are specified in degrees).
    """
    angles_degrees = np.linspace(min_theta, max_theta)
    angles_radians = deg2rad(angles_degrees)
    values = np.sin(angles_radians)
    X = angles_degrees
    Y = values
    plt.plot(X,Y)
    plt.show()

# EXERCISE 2.1 Implement this! Try not to look at the
#  implementation of plot_sine TOO much...
def plot_cosine(min_theta, max_theta):
    """
    Generates a plot of sin(theta) between min_theta
    and max_theta (both of which are specified in degrees).
    """
    angles_degrees = np.linspace(min_theta, max_theta)
    angles_radians = deg2rad(angles_degrees)
    values = np.cos(angles_radians)
    X = angles_degrees
    Y = values
    plt.plot(X,Y)
    plt.show()
