#!/usr/bin/env python

import math as m
import random

def direct_pi(n):
	n_hits = 0
	for i in range(n):
		x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
		if x ** 2 + y ** 2 < 1.0:
			n_hits += 1
	return n_hits

n_trials = 1000000
for attempt in range(10):
	print attempt, 4 * direct_pi(n_trials) / float(n_trials)