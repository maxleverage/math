#!/usr/bin/env python
import numpy as np

n = 28123

# Find all divisors of number n	
def divisors(n):
	result =  []
	for i in range(1, int(np.ceil(np.sqrt(n)))):
		if np.mod(n, i) == 0:
			result.append(i)
	for j in range(1, len(result)):
		result.append(n/result[j])
	return result
	
# Find all abundant number up to and including n
def abundant(n):
	int_list = range(1, n+1)
	index = [0] * len(int_list)
	for i in range(0, n):
		if sum(divisors(int_list[i])) > int_list[i]:
			index[i] = 1
	return np.array(index)
	
# Obtain list of abundant numbers below n
result = abundant(n)
abundant_num = np.where(result==1)[0]
abundant_num += 1

# Check for odd numbers
init = 0
for i in abundant_num:
	if np.mod(i, 2) != 0:
		init += 1
		
print init

# Search through list of abundant numbers
def abundantsum(abundant_list):
	sum = []
	for i in range(0,len(abundant_list)):
		for j in range(i, len(abundant_list)):
			sum.append(abundant_list[i] + abundant_list[j])
	return np.array(sum)

abundant_sum = abundantsum(abundant_num)
new_sum = []
for i in range(0, len(abundant_sum)):
	if abundant_sum[i] <= 28123:
		new_sum.append(abundant_sum[i])
	
new_sum = set(new_sum)
n_abundant = set(range(1,n+1)) - new_sum
n_abundant = n_abundant - set(abundant_num)
sum(n_abundant)

