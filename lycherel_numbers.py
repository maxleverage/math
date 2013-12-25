#!/usr/bin/env python

import math as m
import numpy as np
import time

""" Palindrome Checker """

def ispalindrome(word):
	if len(word) < 2: return True
	if word[0] != word[-1]: return False
	return ispalindrome(word[1:-1])

""" Digit flipper """

def digit_reverser(number):
	return str(number)[::-1]	

""" A number is either palindrome below 50 iterations for n < 10,000 or it is a Lycherel number.
Find all numbers for n < 10,000 for which the first 50 iterations of flip and add procedure 
does not produce a palindrome """

start_time = time.time()
counter = 0
for i in range(1, 10001):
	iter = 0
	digit_sum = i
	while iter < 50:
		digit_sum = digit_sum + int(digit_reverser(digit_sum))
		if ispalindrome(str(digit_sum)):
			break
		if iter == 49:
			counter += 1
		iter += 1

finish_time = time.time() - start_time

print "The number of Lycherel numbers below 10,000 is %i. It took %f seconds to find the solution" % (counter, finish_time)
