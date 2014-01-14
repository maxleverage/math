#!/usr/bin/env python

import math as m
import numpy as np
import time
from fractions import Fraction as F

""" Generate Coefficients """

seed = [2]
for i in xrange(1, 34):
	seed.extend([1, 2*i, 1])


seed.reverse()

""" Digit Sum """

def digit_sum(number):
	s = 0
	while number:
		s += number % 10
		number /= 10
	return s

""" Fraction Addition """

start_time = time.time()

sum = F(1, seed[0]) 
for i in range(1, len(seed)):
	sum = seed[i] + 1/sum

sum = str(sum).split("/")

numerator_sum = digit_sum(int(sum[0]))
finish_time = time.time() - start_time

print "The numerator digit sum of the 100th convergent for e is %i. It took %f seconds to find the solution." % (numerator_sum, finish_time)






