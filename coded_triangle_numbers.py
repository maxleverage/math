#!/usr/bin/env python

import csv
import urllib2
import time

""" Read in letters """

as1 = urllib2.urlopen('https://projecteuler.net/project/words.txt')
webpage = as1.read()
webpage = webpage.split('","')

webpage[0] = webpage[0][1:]
webpage[len(webpage)-1] = webpage[len(webpage)-1][0:(len(webpage[len(webpage)-1])-1)]

""" Triangle Number Generator """

def triangle(n):
	""" Generates the Nth triangle number """
	if n == 1:
		return 1
	else:
		return n + triangle(n-1)

""" Generate List of Triangle Numbers """

start = time.time()
triangle_list = map(triangle, range(1,50))

""" Alphabet Dictionary """

alphabet_dict = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9,
"J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20,
"U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}

""" Coded Triangle Search """

counter = 0
for element in webpage:
	word_sum = 0
	for i in element:
		word_sum += alphabet_dict[i]
	if word_sum in triangle_list:
		counter += 1

finish_time = time.time() - start

print "The number of coded triangle numbers in the words.txt file is %i. It took %f seconds to find the solution" % (counter, finish_time)

