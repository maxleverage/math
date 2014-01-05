#!/usr/bin/env python

import math as m
import numpy as np
import time

""" Prime sieve """

def sieve(number_limit):
	numbers = range(0, number_limit)
	for prime in numbers:
		if prime < 2:
			continue
		elif prime > number_limit ** 0.5:
			break
		for i in range(prime ** 2, number_limit, prime):
			numbers[i] = 0
	return [x for x in numbers if x > 1]


start_time = time.time()

primes = sieve(int(1e8))
prime_set = set(primes)

connected_nodes = {}
for prime in primes:
	s = str(prime)
	for i in range(1, len(s)/2 + 1):
		if s[i] != '0':
			a, b, c, d = int(s[:i]), int(s[i:]), int(s[i:]+s[:i]), int(s[:i]+s[i:])
			if a in prime_set and b in prime_set and c in prime_set and d in prime_set and a != b:
				if b < a:
					a, b = b, a
				if not a in connected_nodes:
					connected_nodes[a] = set()
				connected_nodes[a].add(b)

""" Five Tuple Search """

five_tuples = set()
for a in connected_nodes:
	for b in connected_nodes[a]:
		if b in connected_nodes:
			ab_set = connected_nodes[a] & connected_nodes[b]
			for c in ab_set:
				if c in connected_nodes:
					abc_set = ab_set & connected_nodes[c]
					for d in abc_set:
						if d in connected_nodes:
							abcd_set = abc_set & connected_nodes[d]
							for e in abcd_set:
								five_tuple = (a, b, c, d, e)
								five_tuples.add(five_tuple)

for five_tuple in five_tuples:
	answer = sum(five_tuple)

finish_time = time.time() - start_time

print "The lowest of a five pair prime set is %i. It took %f seconds to find the solution." % (answer, finish_time)


