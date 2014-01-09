#!/usr/bin/env python

import math as m
import numpy as np 
import time

""" Miller Rabin Primality Test """

def decompose(n):
	s = 0
	while n % 2 == 0:
		s += 1
		n /= 2
	return s, n

def isWitness(x, n, s, d):
	x = pow(x, d, n)
	if x == 1 or x == n - 1:
		return False
	for _ in range(s):
		x = pow(x, 2, n)
		if x == n - 1:
			return False
	return True

def isPrime(n, max_iter):
	if n == 2 or n == 3: return True
	if n < 2: return False
	k = 0
	s, d = decompose(n - 1)
	k = 0
	while k < max_iter:
		x = np.random.randint(2, n - 1)
		if isWitness(x, n, s, d):
			return False
		k += 1
	return True

""" Generating Prime Spirals """

start_time = time.time()
number_primes = 3
side_length = 2
c = 9

while number_primes / (2.0 * side_length + 1) > 0.10:
	side_length += 2
	for _ in range(3):
		c += side_length
		if isPrime(c, 25):
			number_primes += 1
	c += side_length

finish_time = time.time() - start_time

print "The side length for which primes to total diagonal numbers falls below 0.1 is %i. It took %f seconds to find the solution." % (side_length+1, finish_time)
