#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		lowestUnique = 10
		pos = 0

		numbers = [int(n) for n in line.rstrip().split()]
		for i, n in enumerate(numbers, start=1):
			if numbers.count(n) == 1:
				if n < lowestUnique:
					lowestUnique = n
					pos = i

		print(pos)