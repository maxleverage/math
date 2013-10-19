#!usr/bin/env python

import math as m

""" Prime checker for a given n """

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

""" Prime sieve """

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

""" Primality check for the search space """

def quad_prime_check(begin, end, number_limit):
	prime_space = sieve(number_limit)
	a_max = 0
	b_max = 0
	n_max = 0
	for a in range(begin,end+1,2):
		for b in prime_space:
			n = 0
			if b == 2:
				a_even = a - 1
				while prime_checker(n*n + a_even*n + b) == 1:
					n += 1
			else:		
				while prime_checker(n*n + a*n + b) == 1:
					n += 1
			if n > n_max:
				a_max = a
				b_max = b
				n_max = n
	return n_max, a_max, b_max, a_max * b_max

print quad_prime_check(-999,1000,1000)

	

