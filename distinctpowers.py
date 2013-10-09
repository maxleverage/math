#!/usr/bin/env python

import math as m

def dpowers(begin,end):
	result = []
	for a in range(begin,(end+1)):
		for b in range(begin,(end+1)):
			if (a ** b) not in result:
				result.append(a ** b)
	return result

distinct_powers = dpowers(2,100)

print len(distinct_powers)
