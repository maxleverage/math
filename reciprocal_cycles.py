#!/usr/bin/env python

import math as m
import time

""" Reciprocal Cycles """

def reciprocal_length(n):
	a = 10
	cycles = [a]
	while True:
		r = int(a / n)
		a = 10 * (a - r * n)
		if a in cycles:
			first = cycles.index(a)
			next = len(cycles)
			break
		cycles.append(a)
	return next - first

""" Iterate Over Numbers """

max_len = 0
max_index = 0
start = time.time()
for i in range(2, 1000):
	length = reciprocal_length(i)
	if length > max_len:
		max_len = length
		max_index = i

print "The value which generates the longest reciprocal length is %i. It took %f seconds to find the solution" % (max_index, time.time() - start)



