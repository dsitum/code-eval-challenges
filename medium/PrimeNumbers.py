#!/usr/bin/env python3

from sys import argv

with open(argv[1], "r") as f:
	for line in f:
		n = int(line.rstrip())
		primes = [True for i in range(n)]
		primes[0] = False 
		primes[1] = False  # zero and one are not primes

		for i in range(2, n):
			if primes[i]:
				for j in range(i*2, n, i):
					primes[j] = False

		print(",".join(str(i) for i,p in enumerate(primes) if p is True))
