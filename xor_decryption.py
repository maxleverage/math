#!/usr/bin/env python

import math as m
import numpy as np
import time
import string
import urllib2

""" Read in encrypted message """

cipher = urllib2.urlopen("https://projecteuler.net/project/cipher1.txt")
cipher_text = cipher.read()
cipher_text = cipher_text.split(",")
cipher_text[-1] = cipher_text[-1][0:2]

key_base = string.lowercase

""" Frequency Analysis """

start_time = time.time()
letter_1 = []
letter_2 = []
letter_3 = []
space_ascii = ord(' ')
for letter in key_base:
	space_counter = 0
	for i in range(0, len(cipher_text), 3):
		if int(cipher_text[i]) ^ ord(letter) == space_ascii:
			space_counter += 1
	letter_1.append(space_counter)
	space_counter = 0
	for j in range(1, len(cipher_text), 3):
		if int(cipher_text[j]) ^ ord(letter) == space_ascii:
			space_counter += 1
	letter_2.append(space_counter)
	space_counter = 0
	for k in range(2, len(cipher_text), 3):
		if int(cipher_text[k]) ^ ord(letter) == space_ascii:
			space_counter += 1
	letter_3.append(space_counter)

""" Secret Key """

key = [ord(key_base[letter_1.index(max(letter_1))]), ord(key_base[letter_2.index(max(letter_2))]), ord(key_base[letter_3.index(max(letter_3))])]

""" Decryption """

decrypted_message = []
for i in range(len(cipher_text)):
	decrypted_message.append(int(cipher_text[i]) ^ key[i % 3])

ascii_sum = sum(decrypted_message)
finish_time = time.time() - start_time

print "The ASCII sum of XOR decrypted message is %i. It took %f seconds to find the solution." % (ascii_sum, finish_time)


