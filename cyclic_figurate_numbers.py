#!/usr/bin/env python

import math as m
import numpy as np
import time
from itertools import permutations

""" Number Definitions """

def triangle(n): return n * (n+1) / 2

def square(n): return n ** 2

def pentagonal(n): return n * (3*n-1) / 2

def hexagonal(n): return n * (2*n-1)

def heptagonal(n): return n * (5*n-3) / 2

def octagonal(n): return n * (3*n-2)

start_time = time.time()
base_list = range(1, 150)
triangle_list = map(triangle, base_list)
triangle_list = [x for x in triangle_list if len(str(x)) == 4]
triangle_list = map(str, triangle_list)

square_list = map(square, base_list)
square_list = [x for x in square_list if len(str(x)) == 4]
square_list = map(str, square_list)

pentagonal_list = map(pentagonal, base_list)
pentagonal_list = [x for x in pentagonal_list if len(str(x)) == 4]
pentagonal_list = map(str, pentagonal_list)

hexagonal_list = map(hexagonal, base_list)
hexagonal_list = [x for x in hexagonal_list if len(str(x)) == 4]
hexagonal_list = map(str, hexagonal_list)

heptagonal_list = map(heptagonal, base_list)
heptagonal_list = [x for x in heptagonal_list if len(str(x)) == 4]
heptagonal_list = map(str, heptagonal_list)

octagonal_list = map(octagonal, base_list)
octagonal_list = [x for x in octagonal_list if len(str(x)) == 4]
octagonal_list = map(str, octagonal_list)

print "Performing depth first search"

def depth_first_search(set_list, depth, match, partial_list):
	if len(partial_list) == len(set_list):
		return partial_list
	for value in set_list[depth]:
		if value[:2] == match:
			partial_list.append(value)
			return depth_first_search(set_list, depth+1, value[2:], partial_list)

combined_list = (square_list, pentagonal_list, hexagonal_list, heptagonal_list, octagonal_list)

def depth_first_search_loop():
	for triangle in triangle_list:
		for perm in permutations(combined_list):
			result = depth_first_search(perm, 0, triangle[2:], [])
			if result is not None:
				if result[-1][2:] == triangle[:2]:
					return [triangle, result]

dfs_result = depth_first_search_loop()
cyclic_sum = int(dfs_result[0])
for number in dfs_result[1]:
	cyclic_sum += int(number)

finish_time = time.time() - start_time

print "The sum of 6 four digit cyclic numbers is %i. It took %f seconds to find the solution." % (cyclic_sum, finish_time)
