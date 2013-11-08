#!/usr/bin/env python

import math as m
import time
from itertools import permutations

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

""" Pandigital Generator """

def pandigital_generator(n):
	""" N defines the number of pandigital digits in each number """
	pandigital_set = range(n)
	pandigital_set = map(str, pandigital_set)
	pandigital_list = []
	for element in permutations(pandigital_set):
		accum = ''
		for a in element:
			accum += a
		pandigital_list.append(accum)
	return pandigital_list

""" Substring divisibility """

def substring_divisibility(input_pandigital):
	""" Takes input pandigital and checks if substring structure is divisible by consecutive primes """
	prime_list = sieve(18)
	prime_list.insert(0,0)
	for i in range(1, 8):
		if int(input_pandigital[(0+i):(3+i)]) % prime_list[i] == 0:
			continue
		else:
			return 0 
	return int(input_pandigital)

""" Check for All 9 Digit Pandigital Numbers """

start = time.time()	
pandigital_sum = sum(map(substring_divisibility, pandigital_generator(10)))

finish_time = time.time() - start

print "The sum of all 0-9 pandigital numbers where its 3 digit substrings are divisible by consecutive prime numbers is %i. It took %f seconds to find the solution" % (pandigital_sum, finish_time)



