#!/usr/bin/env python

import math as m
import time

def champernowne(n):
	""" Function takes n as input """
	champernowne_result = ''
	for i in xrange(1,n+1):
		champernowne_result += str(i)
	return champernowne_result

start = time.time()
d = [1, 10, 100, 1000, 10000, 100000, 1000000]

product = 1
for element in d:
	product *= int(champernowne(element)[element-1])

finish_time = time.time() - start

print "The product of base 10 digits below 1 million in Champernowne's constant is %i. It took %f seconds to find the solution." % (product, finish_time)
