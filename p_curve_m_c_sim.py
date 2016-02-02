# Paul Coster November 2015
#
# A simple monte carlo simulator to investigate p-curves
# using randomly generated numbers. 
#
# By changing the values of effect_size and effect scale you can see that pretty much any slope can be generated in the p-curve.
#

from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# effect_size - a parameter that dictates the shift of the mean from the null position. 
# measured in units of variance of the null curve

effect_size = 0.5

# effect_scale - a parameter that dictates the variance of the treatment distribution from the null effect distirbution. 
# measured in units of variance of the null curve

effect_scale = 0.7


# Generates a set of random numbers distributed normally with parameters dictated by effect_size and effect_scale
# Size dictates the quantity generated
r = norm.rvs(loc=effect_size, scale=effect_scale,size=10000)

# The randomly generated numbers are then binned according to the location of the confidence intervals of the null hypothesis distribution
h = np.histogram(r,[norm.ppf(0.945,0,1),norm.ppf(0.955,0,1),norm.ppf(0.965,0,1),norm.ppf(0.975,0,1),norm.ppf(0.985,0,1),norm.ppf(0.995,0,1)])


# Prints a p-curve
print "P = 0.01: " + str(h[0][4])
print "P = 0.02: " + str(h[0][3])
print "P = 0.03: " + str(h[0][2])
print "P = 0.04: " + str(h[0][1])
print "P = 0.05: " + str(h[0][0])
