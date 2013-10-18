#!/usr/bin/env python

import math as m

""" Prime Checker """

def prime_checker(input_number):
	divisors = []
	for i in range(1, int(input_number ** 0.5)+1):
		if input_number % i == 0:
			divisors.append(i)
	if len(divisors) == 1:
		return 1
	else: return 0

""" Digit Rotator """

def digit_rotator(number):
	""" Enumerates all possible digit rotations of given number n """
	rotation_result = [number]
	digit_length = len(list(str(number)))
	old_digit = list(str(number))
	counter = 1
	while counter < digit_length:
		accum = ''
		new_digit = old_digit
		new_digit.append(new_digit[0])
		new_digit = new_digit[1:len(new_digit)] 
		for string in new_digit:
			accum += string
		rotation_result.append(int(accum))
		old_digit = new_digit
		counter += 1
	return rotation_result

""" Sieve for finding all primes below a given limit N  """

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

""" Circular Checker for Primes """

def circular_checker(number_limit):
	""" Takes as input a set of primes below the given number limit """
	prime_space = sieve(number_limit)
	search_space = set(prime_space)
	for i in prime_space:
		accum = 0
		rotated_digits = digit_rotator(i)
		rotated_set_length = len(rotated_digits)
		""" Checks for primality of each digit in rotated set """
		for digit in rotated_digits:
			accum += prime_checker(digit)
		""" If the accumulator for primality equals the rotated set length, then the base number is a circular prime """
		if accum == rotated_set_length:
			""" We remove the circular primes from the search space if all rotated digits are prime """
			search_space = search_space - set(rotated_digits)
	return len(prime_space) - len(search_space)

print circular_checker(int(1e6))

