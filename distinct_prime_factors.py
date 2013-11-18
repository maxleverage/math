#!/usr/bin/env python

import math as m
import time

""" Sieve for Prime Numbers """

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


""" Prime Factors """

def prime_factors_vector(n):
    """ Takes as input n and returns a list of prime factors """
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d += 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return len(set(factors)) ==	4

""" Iterate Through List of Integers """

start = time.time()
begin = 2 * 3 * 5 * 7
found = False
while not found:
	if sum(map(prime_factors_vector, [begin, begin+1, begin + 2, begin + 3])) == 4:
		found = True
		result = begin
		break
	begin += 1

finish_time = time.time() - start

print "The smallest number which generates a list of four consecutive numbers which have four distinct prime factors is %i. It took %f seconds to find the solution." % (result, finish_time)

