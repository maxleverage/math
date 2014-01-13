#!/usr/bin/env python

import math
import numpy as np
import time

""" Continued Fractions Algorithm """

start_time = time.time()
odd_period = 0
n = 2
for n in range(2, 10001):
	m = 0
	d = 1
	a_0 = math.floor(n ** 0.5)
	if a_0 * a_0 == n:
		continue
	a = a_0
	period = 0
	while a != 2 * a_0:
		m = d * a - m
		d = (n - m * m) / d
		a = math.floor((a_0 + m) / d)
		period += 1
	if period % 2 == 1:
		odd_period += 1

finish_time = time.time() - start_time

print "The number of odd period continuous fraction representations below 10,000 is %i. It took %f seconds to find the solution." % (odd_period, finish_time)
