#!/usr/bin/env python

import csv
import urllib
import urllib2
import re

as1 = urllib2.urlopen("https://projecteuler.net/project/names.txt")
webpage = as1.read()
webpage = webpage.split('","')

webpage[0] = webpage[0][1:len(webpage[0])]
webpage[len(webpage)-1] = webpage[len(webpage)-1][0:(len(webpage[len(webpage)-1])-1)]
webpage.sort()

alphabet_dict = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9,
"J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20,
"U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}

prod_result = []
init_sum = 0
for i in range(0, len(webpage)):
	for j in range(0,len(webpage[i])):
		temp_var = webpage[i][j]
		new_sum = alphabet_dict[temp_var] + init_sum
		init_sum = new_sum
	prod_result.append(new_sum * (i+1))
	init_sum = 0
		
print sum(prod_result)

