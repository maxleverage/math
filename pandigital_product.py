#!/usr/bin/env python

import math as m

""" Find all divisors which do not contain given input_number """

def divisors(input_number):
	divisors = []
	for i in range(2, int(input_number ** 0.5 + 1)):
		if input_number % i == 0:
			divisors.append(i)
	for j in range(len(divisors)):
		divisors.append(input_number/divisors[j])
	divisors.sort()
	return divisors
	
""" Pandigital generator """

def pandigital_generator(input_number):
	""" Computes all divisors of input_number, produces all possible combinations of divisors and concantenates with input_number """
	number_divisors = divisors(input_number)
	sieve = []
	pandigital_result = []
	if '0' in str(input_number):
		return pandigital_result
	else:
		for i in range(len(number_divisors)):
			if len(set(str(number_divisors[i])+str(number_divisors[len(number_divisors)-i-1]))) == len(str(number_divisors[i])+str(number_divisors[len(number_divisors)-i-1])) & len(str(number_divisors[i])+str(number_divisors[len(number_divisors)-i-1])) == 9 - len(str(input_number)):
				sieve.append(str(number_divisors[i])+str(number_divisors[len(number_divisors)-i-1]))
		for j in range(len(sieve)):
			if set(str(input_number)) & set(sieve[j]) == set():
				pandigital_result.append(sieve[j]+str(input_number))
	return pandigital_result

""" Pandigital checker """

def pandigital_checker(input_number):
	pandigital_set = {'1','2','3','4','5','6','7','8','9'}
	pandigital_list = pandigital_generator(input_number)
	counter = 0
	if pandigital_list == []:
		return 0
	else:
		for i in pandigital_list:
			pandigital = set(i)
			if pandigital == pandigital_set:
				counter += 1
			if counter > 0:
				return input_number
				break
			

""" Iterate of all numbers below given limit """

def pandigital_iterator(n_limit):
	""" Checks for pandigital solutions up to given n_limit """
	""" No pandigital numbers below 1500 """
	counter = 4000
	pandigital_result = []
	while counter < n_limit:
		if pandigital_checker(counter) > 0:
			pandigital_result.append(counter)
		counter += 1
	return pandigital_result

n_limit = int(1e5)
print sum(pandigital_iterator(n_limit))
