#!/usr/bin/env python

import math as m
import numpy as np
import time

start_time = time.time()
n = 1
lower = 0
counter = 0
while lower < 10:
	lower = m.ceil(10 ** ((n - 1.0)/n))
	counter += 10 - lower
	n += 1

finish_time = time.time() - start_time

print "The number of digits for which digit length matches exponent is %i. It took %f seconds to find the solution." % (counter, finish_time)