#!/usr/bin/env python

import math as m
import numpy as np
import time

""" Search Space Definition """

def sieve(number_limit):
        """ Checks for all primes below a given number limit """
        numbers = range(0, number_limit)
        for prime in numbers:
                if prime < 2:
                        continue
                elif prime > number_limit ** 0.5:
                        break
                for i in range(prime ** 2, number_limit, prime):
                        numbers[i] = 0
        return [x for x in numbers if x > 1] 

""" Cumulative Sum of Prime List """

def cumulative_sum(prime_list):
	result = []
	prime_sum = 0
	for prime in prime_list:
		prime_sum += prime
		result.append(prime_sum)
	return result

""" Cumulative Sum Difference List """

def difference_list(prime_sum_list, number_limit):
	difference = []
	prime_length = []
	length = len(prime_sum_list)
	for i in xrange(0, length):
		for j in xrange(i+1, length):
			if prime_sum_list[j] - prime_sum_list[i] >= number_limit:
				break
			else:
				difference.append(prime_sum_list[j] - prime_sum_list[i]) 
				prime_length.append(j - i)
	return difference, prime_length

""" Energy Function """

def compute_energy(input_prime, prime_sum_list, number_limit, difference, prime_position):
	if input_prime in prime_sum_list:
		return -prime_sum_list.index(input_prime) + 1
	else:
		length = len(difference)
		for i in range(length):
				if difference[i] == input_prime:
					return -prime_position[i]
					break
	return 0

""" Quantum Annealing for Prime Length Search """

print "Running quantum annealing"

def quantum_annealing_search(start_field_strength, field_strength_decay, width, max_limit, max_iter):
	start = time.time()
	prime_list = sieve(max_limit)
	prime_sum_list = cumulative_sum(prime_list)
	difference, primes = difference_list(prime_sum_list, max_limit)
	initial_state = prime_list[np.random.randint(0, len(prime_list))]
	initial_energy = compute_energy(initial_state, prime_sum_list, max_limit, difference, primes)
	iter = 0
	while iter < max_iter:
		new_state = prime_list[np.random.randint(0, len(prime_list))]
		new_energy = compute_energy(new_state, prime_sum_list, max_limit, difference, primes)
		if new_energy < initial_energy:
			initial_state = new_state
			initial_energy = new_energy
			start_field_strength = 1 - field_strength_decay
		elif new_energy == initial_energy:
			start_field_strength = start_field_strength * (1 - field_strength_decay/5)
		elif new_energy > initial_energy:
			if np.exp(-((new_energy - initial_energy) ** 0.5) * width / start_field_strength) > np.random.random():
				initial_energy = new_energy
				initial_state = new_state
				start_field_strength = 1 - field_strength_decay
			else: 
				start_field_strength = start_field_strength * (1 - field_strength_decay/5)
		iter += 1
	finish_time = time.time() - start
	return initial_state, -initial_energy, finish_time

counter = 0
while counter < 50:
	print quantum_annealing_search(100,0.06,5,100000,1000)
	counter += 1


