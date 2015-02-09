#!/usr/bin/env python3

from sys import argv

with open(argv[1], "r") as f:
	for line in f:
		numbers = [int(i) for i in line.rstrip().split()]
		numbers.pop(0)  # popping out first number (as it's not part of sequence)
		n = len(numbers)

		if n == 1:
			print("Jolly")
			break


		diffs = set()

		for i in range(1, n):
			diff = abs(numbers[i-1] - numbers[i])
			if diff not in diffs:
				diffs.add(diff)
			else:
				break

		unused = (set(range(1, n))).difference(diffs)

		if not unused:
			print("Jolly")
		else:
			print("Not jolly")
