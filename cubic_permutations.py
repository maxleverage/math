#!/usr/bin/env python

import math as m
import numpy as np
import time

""" Cubic Value Sort """

def cubic_sort(cube):
	cube_string = [x for x in cube]
	cube_string.sort()
	cube_out = ""
	for digit in cube_string:
		cube_out += digit
	return cube_out

""" Dictionary Search """

print "Performing dictionary search"

start_time = time.time()
cubes_sorted = {}
for i in xrange(1,10000):
	cube = str(i ** 3)
	cubes_sorted[cube] = cubic_sort(cube) # Key / value assignment
cube_values = cubes_sorted.values()
cube_keys = cubes_sorted.keys()
cube_keys.sort()
cube_candidates = []
for k in cube_keys:
	if cube_values.count(cubes_sorted[k]) == 5:
			cube_candidates.append(int(k))

answer = min(cube_candidates)
finish_time = time.time() - start_time

print "The minimum cube which generates a 5 member permuted cube family is %i. It took %f seconds to find the solution." % (answer, finish_time)