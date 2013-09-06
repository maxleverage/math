#!/usr/bin/env python

import math as m

def factorial(n):
	if(n == 0):
		return 1
	else:
		return n * factorial(n-1)

print(str(factorial(100)))

str = str(factorial(100))

output = []
i = 0

while i < len(str):
	output.append(str[i])
	i += 1

for i in xrange(0, len(output)):
	output[i] = int(output[i])

print(sum(output))
