#!/usr/bin/env python

import math as m
import time
import sys

sys.setrecursionlimit(1500)

""" Ten digits """

def ten_digits(n):
    if n == 1:
        return 1
    else:
        return ten_digits(n-1) + (n ** n) 

start = time.time()
digits = str(ten_digits(1000))
digits_result = int(digits[2991:len(digits)])
finish_time = time.time() - start

print "The last ten digits of the 1000 self power sum is %i and it took %f seconds to find the solution." \
% (digits_result, finish_time)

