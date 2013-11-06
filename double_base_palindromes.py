#!/usr/bin/env python

import math as m
import time

""" Decimal to Binary """

def dec2bin(n):
	""" Takes decimal nput n and converts to binary """
	if n == 0: return ''
	else: 
		return dec2bin(n/2) + str(n%2)

""" Palindrome Checker """

def palindrome_check(n):
	n = str(n)
	if len(n) <= 1:
		return True
	else:
		return n[0] == n[-1] and palindrome_check(n[1:-1])

""" Double Base Palindromes Less Than 1 Million """
start = time.time()
counter = 1
palindrome_result = []
while counter < int(1e6):
	if palindrome_check(counter) and palindrome_check(dec2bin(counter)):
		palindrome_result.append(counter)
	counter += 1

finish_time = time.time() - start

print "The sum of all double base palindromes below 1 million is %i and it took %f seconds to find the solution" % (sum(palindrome_result), finish_time)


