#!/usr/bin/env python3

from sys import argv

with open(argv[1], "r") as f:
	for line in f:
		n = int(line.rstrip())

		ones = 0
		while n > 0:
			ones += n % 2
			n = int(n/2)

		print(ones)
