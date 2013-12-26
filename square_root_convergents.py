#!/usr/bin/env python

import math as m
import numpy as np
import time

start_time = time.time()
numerator = 1; denominator = 2; counter = 0
for i in range(1, 1001):
	numerator += 2*denominator; new_numerator = denominator
	new_denominator = numerator; denominator = new_denominator; numerator = new_numerator
	if len(str(numerator+denominator)) > len(str(denominator)):
		counter += 1
finish_time = time.time() - start_time

print "The number of fractions where the numerator exceeds the denominator in digit length for the first 1,000 expansions is %i. \
It took %f seconds to find the solution." % (counter, finish_time)
