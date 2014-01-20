#!/usr/bin/env python

import math as m
import numpy as np
import time

""" GCD """

def gcd(a, b):
	while b:
		a, b = b, a%b
	return a

""" Bounded Solution """

start_time = time.time()

a = 3
b = 7
n = 0
d = 1
lowerbound = 2
q = int(1e6)

while q >= lowerbound:
	p = (a * q - 1) / b
	if p * d > n * q:
		d, n = q, p
		lowerbound = d / (a * d - b * n)
	q -= 1

factor = gcd(n, d)
n /= factor
d /= factor

finish_time = time.time() - start_time

print "The smallest ordered fraction to the left of 3/7 has numerator %i. It took %f seconds to find the solution." % (n, finish_time)