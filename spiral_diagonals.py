#!/usr/bin/env python

import math as m
import time

""" Sum of squares """

def diagonal_sum(n):
	""" Takes matrix of size n and computes diagonal sum """
	if n == 0:
		return 1
	else:
		return 4*((2*n+1)**2) - 12 * n + diagonal_sum(n-1)

print "The diagonal sum for an 1001 x 1001 matrix is %f." % (diagonal_sum(500))

""" Analytical solution for spiral sum """

def spiral_sum(n):
	start = time.time()
	return (16.0/3.0) * (n ** 3) + 10.0 * (n ** 2) + (26.0/3.0) * n + 1, time.time() - start

print "The diagonal sum for an 1001 x 1001 matrix is %f. It took %f seconds to find the solution" % (spiral_sum(500))
