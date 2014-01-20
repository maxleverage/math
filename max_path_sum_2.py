#!/usr/bin/env python

import math as m
import numpy as np
import urllib2
import time

""" File Access """

triangle = urllib2.urlopen("https://projecteuler.net/project/triangle.txt")
triangle = triangle.read()
triangle = triangle.split("\n")[0:-1]
triangle = [[int(s) for s in row.split(" ")] for row in triangle]

""" Dynamic Programming """
start_time = time.time()

for i in xrange(len(triangle)-2, -1, -1):
	for j in xrange(len(triangle[i])):
		triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])

finish_time = time.time() - start_time

print "The maximum path sum of a 100 row triangle is %i. It took %f seconds to find the solution." % (triangle[0][0], finish_time)
