#!/usr/bin/env python3 

primes = [True for i in range(1000)]
for i in range(2, 1000):
	if primes[i]:
		j = i * 2
		while j < 1000:
			primes[j] = False
			j += i

for i in range(999, 1, -1):
	if primes[i] and str(i) == str(i)[::-1]:
		print(i)
		break