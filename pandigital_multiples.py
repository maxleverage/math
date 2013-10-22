#!/usr/bin/env python

import math as m

""" Search for largest of 1-9 pandigital number """

def pandigital_checker(input_number):
	pandigital_set = {'1','2','3','4','5','6','7','8','9'}
	counter = 0
	if pandigital_set - set(str(input_number)) == set():
		return 1 
	else:
		return 0

""" Pandigital Multiple Search """
""" Number we are looking for must be less than 5 digits. We know the first digit must begin with a 9.
1) If fixed input is 2 digit number beginning with a 9, we will end with a 8 digit number
2) If fixed input is 3 digit number beginning with a 9, we will end with a 7 digit number
3) If fixed input is 4 digit number beginning with a 9, multiplication by 2 yields a 5 digit second number which when concantenated with the first yields a 9 digit number 

We can limit the solution space to between 9123 as the lower bound, since doubling 9122 yields two 4s
The upper bound must be less than 9877 since doubling yields two 4s

Further more, the second digit in the lower bound cannot be a 1 since doubling 9123 yields two 1s when concatenated so the lower bound is 9234
The upper bound can be further reduced to 9

"""

def pandigital_multiple_search(lower_bound, upper_bound, pandigital_limit):
	""" Iterates over pandigital numbers generated by concatenating an integer with an ordered, increasing list of integers """
	search_space = range(lower_bound, upper_bound+1)
	output = []
	for element in search_space:
		accum = str(element) + str(2*element)
		if pandigital_checker(int(accum)) == 1:
			output.append(int(accum))
	return output

print max(pandigital_multiple_search(9234,9487,9))






