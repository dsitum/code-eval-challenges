#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		numbers = [float(n) for n in line.strip().split()]
		
		sortedNumbers = sorted(numbers)
		for i,n in enumerate(sortedNumbers, start=1):
			if i < len(sortedNumbers):
				print("{0:.3f}".format(n), end=" ")
			else:
				print("{0:.3f}".format(n), end="")

		print()