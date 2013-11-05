#!/usr/bin/env python

import math as m
import time

""" Curious Fraction Checker """

def curious_fraction(numerator, denominator):
	if numerator < denominator:
		initial_result = float(numerator) / denominator
		numerator = str(numerator)
		denominator = str(denominator)
		for i in numerator:
			for j in denominator:
				numerator_cancel = [x for x in numerator if x != i]
				denominator_cancel = [x for x in denominator if x != j]
				if (numerator_cancel == denominator_cancel) and (float(i)/float(j) == initial_result):
					output_result = str(i) + '/' + str(j)
					return output_result
					break
				else: 
					output_result = 0
		return output_result
	else: return 0


""" Iterate until all curious fractions are found """
""" There are four curious fractions """

start = time.time()
exclusion_list = [10,11,20,22,30,33,40,44,50,55,60,66,70,77,80,88,90,99]
numerator_list = range(10,99)
numerator_list = [x for x in numerator_list if x not in exclusion_list]
denominator_list = range(11,99)
denominator_list = [x for x in denominator_list if x not in exclusion_list]
fraction_result = []
for i in numerator_list:
	for j in denominator_list:
		if type(curious_fraction(i,j)) == str:
			fraction_result.append(str(i) + '/' + str(j))

""" Multiply Fraction Result """

numerator_product = 1
for element in fraction_result:
	numerator_product *= int(element[0:2])


denominator_product = 1
for element in fraction_result:
	denominator_product *= int(element[3:])

""" GCD """

def gcd(a,b):
	while b:
		a, b = b, a % b
	return a

""" Lowest Common Denominator """

lowest_common_denominator = denominator_product / gcd(denominator_product, numerator_product)
finish_time = time.time() - start
print "The solution is %i and it took %f seconds to find the solution" % (lowest_common_denominator, finish_time)

