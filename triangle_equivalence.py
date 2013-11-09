#!/usr/bin/env python

import math as m
import time

""" Pentagonal Number """

def pentagonal_inverse(n):
	""" Takes as input n (integer or pentagonal number) and computes the inverse """
	inverse = (m.sqrt(24 * n + 1) + 1) / 6
	return inverse == int(inverse)

""" Hexagonal Number """

def hexagonal(n):
	return (n * (2 * n - 1))

""" Iterate over lists """

start = time.time()
i = 143
notFound = True
while notFound:
	i += 1
	if pentagonal_inverse(hexagonal(i)) == True:
		notFound = False
		break

result = hexagonal(i)
finish_time = time.time() - start

print "The next triagonal, pentagonal, hexagonal number is %i. It took %f seconds to find the solution." % (result, finish_time)

