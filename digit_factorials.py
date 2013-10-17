#!/usr/bin/env python

print "Importing packages"
import math as m

""" Curious number checker """

def curious_number(input_limit):
	init = 3
	curious_result = []
	while init < input_limit:
		digits = list(str(init))
		accum = 0
		for i in digits:
			accum += m.factorial(int(i))
			if accum == init:
				curious_result.append(init)
		init += 1
	return curious_result


print sum(curious_number(1e6))

