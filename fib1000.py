#!/usr/bin/env python

import numpy as np

fib_mat = np.mat([[0,1], [1,1]])
old_mat = fib_mat
init = 1
while len(str(old_mat[1,1])) < 1000:
	new_mat = old_mat * fib_mat
	old_mat = new_mat
	init  += 1

print init

	

