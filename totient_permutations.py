#!/usr/bin/env python

import math as m
import numpy as np 
import time
from itertools import combinations

""" Prime Sieve """

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

pairs = combinations(sieve(2*int(m.sqrt(1e7))), 2)
minimal = [100, 0]
for n, t in ((a*b, (a-1)*(b-1)) for a, b in pairs if a*b < 1e7):
	ratio = float(n) / t
	if ratio < minimal[0] and sorted(str(n)) == sorted(str(t)):
		minimal = [ratio, n]

finish_time = time.time() - start_time

print "The value which gives the lowest totient ratio and which has a totient value as a permutation of itself is %i. \
It took %f seconds to find the solution." % (minimal[1], finish_time)
