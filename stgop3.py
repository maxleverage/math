#!/usr/bin/env python

int_list = range(100,1000,10)

for i in range(len(int_list)):
	int_list[i] = str(int_list[i])

result = []
for i in range(len(int_list)):
	result.append(int(int_list[i]) - int(int_list[i][::-1]))

for i in range(len(result)):
	result[i] = str(result[i])

new_result = []	
for i in range(len(result)):
	new_result.append(int(result[i]) + int(result[i][::-1]))
	
print max(new_result)


