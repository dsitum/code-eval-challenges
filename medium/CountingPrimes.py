#!/usr/bin/env python3

from sys import argv

with open(argv[1], "r") as f:
	for line in f:
		n, m = [int(i) for i in line.rstrip().split(",")]
		if n > m:
			print(0)
			break

		primes = [True for _ in range(m+1)]
		primes[0] = False
		primes[1] = False

		for i in range(2, m+1):
			if primes[i]:
				for j in range(i*2, m+1, i):
					primes[j] = False

		total = 0

		for i in range(n, m+1):
			if primes[i]:
				total += 1

		print(total)
