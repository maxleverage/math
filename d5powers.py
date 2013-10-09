#!/usr/bin/env python

import math as m

def digit_power_convert(n, exponent):
	str_num = str(n)
	accumulator = 0
	for i in str_num:
		accumulator += int(i) ** exponent
	return accumulator

def digit_power_sum(exponent, max_iter):
	init = 2
	result = [] 
	while init < max_iter:
		if digit_power_convert(init, exponent) == init:
			result.append(init)
		init += 1
	return result

digit_result = digit_power_sum(5, 1e6)
print sum(digit_result)

