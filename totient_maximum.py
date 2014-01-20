#!/usr/bin/env python

import math as m
import numpy as np
import time

""" Sieve """

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

start_time = time.time()

prime_set = sieve(1000)
num = 1
for prime in prime_set:
	num *= prime
	if num > int(1e6):
		max_totient = num / prime
		break

finish_time = time.time() - start_time

print "The maximum value of n totient ratio for n below 1,000,000 is %i. It took %f seconds to find the solution." % (max_totient, finish_time)