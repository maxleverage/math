#!/usr/bin/env python

import math as m
import time

""" Pentagonal Numbers """

def pentagonal_number(n):
	""" Computes nth pentagonal number """
	return n * (3 * n - 1) / 2

pentagonal_list = map(pentagonal_number, range(201))

""" Pentagonal Number Inverse Function """

def pentagonal_inverse(n):
	""" Takes as input n (integer or pentagonal number) and computes the inverse """
	inverse = (m.sqrt(24 * n + 1) + 1) / 6
	return inverse == int(inverse)

""" Iterate for finding pentagonal number """

start = time.time()
i = 0
notFound = True
while notFound:
	i += 1
	n = pentagonal_number(i)
	for j in xrange(i-1, 0, -1):
		k = pentagonal_number(j)
		if pentagonal_inverse(n-k) & pentagonal_inverse(n+k):
			D = abs(n-k)
			notFound = False
			break

finish_time = time.time() - start

print "The pair of pentagonal numbers whose sum and difference is pentagonal and which generates the minimum absolute difference is %i, %i and their difference is %i. \
It took %f seconds to find the solution." % (i, j, D, finish_time)




