#!/usr/bin/env python

import math as m
import time

""" "Pythagorean triples brute force search """

""" a^2 + b^2 = c^2 
s.t. a + b + c = p 
c = p - (a+b)
c^2 = p^2 - 2p(a+b) + (a+b)^2
a^2 + b^2 = p^2 - 2ap - 2bp + a^2 + b^2 + 2ab
2ap - p^2 = 2ab - 2bp
b(2a-2p) = 2ap - p^2
b = (2ap - p^2)/(2a-2p)
"""

def triples_seq_search(max_p):
	start = time.time()
	perimeter_range = range(2,max_p,2)
	optimal_counter = 0
	result = 0
	for p in perimeter_range:
		counter = 0
		for a in range(1,int(m.ceil(p/3))):
			if p * (p - 2 * a) % (2 * (p-a)) == 0:
				counter += 1
		if counter > optimal_counter:
			optimal_counter = counter
			result = p
	return result, time.time() - start

print "The solution is %d and it took %d seconds." % triples_seq_search(1000)




