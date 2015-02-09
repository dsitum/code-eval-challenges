#!/usr/bin/env python3

from sys import argv

with open(argv[1], "r") as f:
	for line in f:
		numbers, k = line.rstrip().split(";")
		numbers = [int(i) for i in numbers.split(",")]
		k = int(k)
		rev = []

		while (k <= len(numbers)):
			for i in range(k-1, -1, -1):
				rev.append(numbers.pop(i))

		rev.extend(numbers)

		print(",".join(str(i) for i in rev))
