#!/usr/bin/env python

import math as m
import numpy as np
import time

""" Digit Sum """

def digit_sum(n):
	s = 0
	while n:
		s += n % 10
		n /= 10
	return s

""" Search Space """

start_time = time.time()
search_space = []
for a in xrange(1, 100):
	for b in xrange(1, 100):
		search_space.append(a ** b)

max_val = 0
for element in search_space:
	new_val = digit_sum(element)
	if new_val > max_val:
		max_val = new_val

finish_time = time.time() - start_time

print "The largest digit sum a, b less than 100 is %i. It took %f seconds to find the solution." % (max_val, finish_time)