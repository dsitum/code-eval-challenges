#!/usr/bin/env python3

from sys import argv

with open(argv[1], "r") as f:
	for line in f:
		numbers = [int(i) for i in line.rstrip().split(",")]
		n = len(numbers)
		largestSum = sum(i for i in numbers if i < 0)
		
		for i in range(n):
			for j in range(i, n):
				s = sum(numbers[i:j+1])
				if s > largestSum:
					largestSum = s

		print(largestSum)
