#!/usr/bin/env python

import math as m
import time
import numpy as np
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

""" Digit Permutations """

def digit_permutations(input_number):
	def string_sum(input_list):
                accum = ''
                for i in input_list:
                        accum += i
                return int(accum)
        result = []
        for perm in permutations(str(input_number)):
                result.append(string_sum(perm))
        return result

""" Find Numbers in Prime List Which Have Constant Difference """

start = time.time()
prime_list = np.array(sieve(int(1e4)))
prime_list = prime_list[np.where(prime_list > 1000)[0]]
exclusion_list = [1487, 4817, 8147]
prime_list = [x for x in prime_list if x not in exclusion_list]

found = False
index = 0
while not found:
        final_result = []
        perm_result = []
        differences = []
        base = prime_list[index]
        number_perm = digit_permutations(base)
        for i in number_perm:
                if (i in prime_list) and (i > base):
                        perm_result.append(i)
        for element in perm_result:
                differences.append(element - base)
        for diff in differences:
                if ((base + diff) in perm_result) and ((base + 2 * diff) in perm_result):
                        final_result.extend([str(base), str(base + diff), str(base + 2 * diff)])
                        found = True
                        break
        index += 1

prime_permutations = ''
for prime in final_result:
        prime_permutations += prime

prime_permutations = int(prime_permutations)

finish_time = time.time() - start

print "The concantenation of the second four digit prime permutation is %i. It took %f seconds to find the solution." % (prime_permutations, finish_time)


