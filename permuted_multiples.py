#!/usr/bin/env python

import math as m
import numpy as np
import time

""" Digit set checker """

def digit_checker(input_number, number_product):
	""" Takes the input number and checks if the same set of digits are in the multiplied number """
	if set(str(input_number)) == set(str(number_product*input_number)) :
		return 1
	else:
		return 0

""" Iterative search """

start_time = time.time()
start = 125874
found = False
while not found:
	permuted_bin_list = [digit_checker(start, product) for product in range(2, 7)]
	if sum(permuted_bin_list) == 5:
		found = True
		break
	start += 1

finish_time = time.time() - start_time

print "The number which has the same set of base digits when multipled by 2, 3, 4, 5, 6 is %i. It took %f seconds to find the solution" % (start, finish_time)
