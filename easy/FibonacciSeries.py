#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		n = int(line)
		f0 = 0
		f1 = 1
		count = 1

		if (n == 0):
			print(0)
		elif (n == 1):
			print(1)
		else:
			while (count < n):
				sum = f0 + f1
				f0 = f1
				f1 = sum
				count += 1

			print(f1)