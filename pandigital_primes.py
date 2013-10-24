#!/usr/bin/env python

import math as m
import time

""" Largest pandigital number is 987654321. We begin searching down. 
If the sum of digits of a given number is divisible by 3, then that number is also divisible by 3
Enumerating:
1+2+3+4+5+6+7+8+9 = 45
1+2+3+4+5+6+7+8 = 36
1+2+3+4+5+6+7 = 28
1+2+3+4+5+6 = 21
1+2+3+4+5 = 15
1+2+3+4 = 10
1+2+3 = 6
1+2 = 3
1 = 1

Hence pandigital numbers of length 7 and 4 will contain primes since the rest are divisible by 3 and rule them 
out as primes. Hence we can reduce our search space and search down from 7654321
"""

""" Prime checker """

def prime_checker(input_number):
	divisors = []
	if input_number < 0:
		return 0
	elif input_number == 1:
			return 0
	else:
		for i in range(1, int(m.sqrt(input_number)+1)):
			if input_number % i == 0:
				divisors.append(i)
		if len(divisors) == 1:
			return 1
		else: return 0

""" Sieve for primes """

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

""" Pandigital checker """

def pandigital_checker(input_number, pandigital_set): 
	""" Checks if a given input number is pandigital """
	if pandigital_set - set(str(input_number)) == set():
		return 1
	else:
		return 0

""" Pandigital prime search """

def pandigital_prime(max_limit):
	""" Takes as input the maximum limit and begins searching down from that limit """
	start = time.time()
	prime_space = sieve(max_limit)
	prime_result = 0
	for i in range(len(prime_space)-1,-1,-1):
		if pandigital_checker(prime_space[i],{'1','2','3','4','5','6','7'}) == 1:
			prime_result = prime_space[i]
			break
	return prime_result, time.time() - start

""" Brute force search from max index """

def pandigital_prime_2(max_limit):
	start = time.time()
	prime_result = 0
	for i in range(max_limit,int(1e6)-1,-1):
		if pandigital_checker(i,{'1','2','3','4','5','6','7'}) & prime_checker(i) == 1:
			prime_result = i
			break
	return prime_result, time.time() - start


print "The largest pandigital prime is %d and it took %f seconds to find this solution." % pandigital_prime(7654321)

print "The largest pandigital prime is %d and it took %f seconds to find this solution." % pandigital_prime_2(7654321)


