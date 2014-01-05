#!/usr/bin/env python

import math as m
import numpy as np
import time

""" Prime Sieve """

def sieve(number_limit):
	numbers = range(0, number_limit)
	for prime in numbers:
		if prime < 2:
			continue
		elif prime > number_limit ** 0.5:
			break
		for i in range(prime ** 2, number_limit, prime):
			numbers[i] = 0
	return [x for x in numbers if x > 1]

""" Prime Checker """

def prime_checker(n):
	if n <= 1:
		return False
	elif n < 4:
		return True
	elif n % 2 == 0:
		return False
	elif n < 9:
		return True
	elif n % 3 == 0:
		return False
	upper_limit = m.floor(m.sqrt(n))
	f = 5
	while f <= upper_limit:
		if n % f == 0:
			return False
		elif n % (f + 2) == 0:
			return False
		f += 6
	return True

start_time = time.time()
smallest_answer = int(1e6)
prime_list = sieve(int(1e6))

for digit in [0, 1, 2]:
	for prime in prime_list:
		p = str(prime)
		if p[:-1].find(str(digit)) > -1:
			strikes = digit
			replacement_digit = digit + 1
			while strikes < 3:
				test_number = p[:-1].replace(str(digit), str(replacement_digit)) + p[-1]
				if not prime_checker(int(test_number)):
					strikes += 1
				replacement_digit += 1
				if replacement_digit > 9 and strikes < 3:
					answer = int(p)
					if answer < smallest_answer:
						smallest_answer = answer
					break

finish_time = time.time() - start_time

print "The smallest prime to form an 8 member prime digit replacement family is %i. \
It took %f seconds to find the solution." % (smallest_answer, finish_time)

