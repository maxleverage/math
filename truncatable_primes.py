#!/usr/bin/env python

import math as m

""" Prime Checker """

def prime_checker(input_number):
	""" Determines if an input number is prime """
	divisors = []
	if input_number == 1:
		return 0
	else:
		for i in range(1, int(input_number ** 0.5)+1):
			if input_number % i == 0:
				divisors.append(i)
		if len(divisors) == 1:
			return 1
		else: return 0

""" Truncator for input_number """

def digit_truncator(input_number, mode):
	""" Generates a set of truncated of numbers. Left or right depending on selection """
	""" Modal selection is 'l' for left truncation or 'r' for right truncation """
	truncated_result = [input_number]
	if mode == "l":
		input_number_str = str(input_number)
		input_length = len(input_number_str)
		if input_length == 1:
			return truncated_result
		else: 
			for i in range(1, input_length):
				truncated_result.append(int(input_number_str[i:input_length]))
			return truncated_result
	elif mode == "r":
		input_number_str = str(input_number)
		input_length = len(input_number_str)
		if input_length == 1:
			return truncated_result
		else: 
			for i in range(-(input_length-1), 0):
				truncated_result.append(int(input_number_str[-input_length:i]))
			return truncated_result

""" Eratosthenes Sieve for finding primes """
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

""" Truncated prime checker """

def truncate_prime_checker(prime, mode):
	truncated_primes = digit_truncator(prime, mode)
	accum = 0
	for digit in truncated_primes:
		accum += prime_checker(digit)
	if accum == len(truncated_primes):
		return 1
	else: return 0

""" Check if given truncated sequences are prime """

def truncatable_prime(prime_limit, search_limit):
	truncatable_prime = []
	init = 0
	prime_list = sieve(search_limit)
	while init < prime_limit:
		for i in range(4, len(prime_list)):
			if truncate_prime_checker(prime_list[i], mode='l') & truncate_prime_checker(prime_list[i], mode='r') == True:
				truncatable_prime.append(prime_list[i])
				init += 1
	return truncatable_prime

print sum(truncatable_prime(11, int(1e6)))


