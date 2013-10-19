#!/usr/bin/env python

import math as m

grid_size = 20

paths = 1
for i in range(0,20):
	paths *= (2*grid_size) - i
	paths /= i + 1

print paths
