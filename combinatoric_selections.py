#!/usr/bin/env python

import math as m
import numpy as np
import time

""" Factorial """

def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)

""" Combinatoric selections """

def combinatoric(n, r):
	return factorial(n) / (factorial(r) * factorial(n - r))

start_time = time.time()

n = 23
counter = 0
while n < 101:
	for r in range(1, n):
		if combinatoric(n, r) > int(1e6):
			counter += 1
	n += 1

finish_time = time.time() - start_time

print "THe number of combinatoric selections which exceed 1 million for 1 <= n <= 100 is %i. It ook %f seconds to find the solution." % (counter, finish_time)
