#!/usr/bin/env python

import math as m
import numpy as np
import time
from itertools import permutations

""" Cube Root Function """

def isCube(number, epsilon):
	cube_root = number ** (1/3.0)
	if m.ceil(cube_root) - cube_root < epsilon: return True
	else: return False

""" Search for 5 Family Permuted Cube """

print "Searching for 5 member cube family"

start_time = time.time()
number = 345
found = False
while not found:
	cube_number = number ** 3
	cube_length = len(str(cube_number))
	counter = 0
	permuted_set = set()
	for perm in permutations(str(cube_number)):
		permuted_cube = ''
		for element in perm:
			permuted_cube += element
		if len(str(int(permuted_cube))) == cube_length:
			permuted_set.add(int(permuted_cube))
	for cube in permuted_set:
		if isCube(cube, 1e-12):
			counter += 1
	if counter == 5:
		found = True
		break
	print number
	number += 1

finish_time = time.time() - start_time

print "The smallest cube to generate a 5 member permuted cube family is %i. It took %f seconds to find the solution." % (cube_number, finish_time)