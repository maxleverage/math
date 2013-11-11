#!/usr/bin/env python

import math as m
import time

""" Eratosthenes Sieve """

def sieve(number_limit):
        """ Checks for all primes below a given number limit """
        numbers = range(0, number_limit)
        for prime in numbers:
                if prime < 2:
                        continue
                elif prime > number_limit ** 0.5:
                        break
                for i in range(prime ** 2, number_limit, prime):
                        numbers[i] = 0
        return [x for x in numbers if x > 1] 

""" Checks if given input is square """

def is_square(n):
	sqrt = n ** 0.5
	return sqrt == int(sqrt)

""" Generate List """

start = time.time()
composite = 1
notFound = True
prime_list = sieve(int(1e4))
while notFound:
	composite += 2
	i = 0
	notFound = False
	while composite >= prime_list[i]:
		if is_square((composite - prime_list[i])/2):
			notFound = True
			result = composite
			break
		i += 1 

finish_time = time.time() - start

print "The smallest odd composite which cannot be written as the sum of a prime and twice a square is %i. It took %f seconds to find the solution." % (composite, finish_time)
