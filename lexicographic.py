#!/usr/bin/env python

import math as m
from itertools import combinations
from itertools import permutations

""" 10! possible arrangements of the ten digits, find the 1 millionth one """

""" Factorial function """

def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

""" Lexicographic search """

def lex_search(ordered_list, n_digit):
	begin_index = 0
	digits = []
	output = ''
	for i in range(0,3):
		digit_counter = i
		while begin_index + factorial(len(ordered_list)-(i+1)) < n_digit:
			begin_index += factorial(len(ordered_list)-(i+1))
			digit_counter += 1
		digits.append(digit_counter)
	first_set = set(digits)
	set_permutations = list(permutations(set(ordered_list)-first_set))
	set_index = n_digit - begin_index - 1
	remaining_digits = set_permutations[set_index]
	for a in digits:
		output += str(a)
	for b in remaining_digits:
		output += str(b)
	return int(output)

print lex_search([0,1,2,3,4,5,6,7,8,9], int(1e6))




