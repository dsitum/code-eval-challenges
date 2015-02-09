#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		numbers, pattern = line.rstrip().split()

		if pattern.find("+") != -1:
			op = "+"
			ind = pattern.find("+")
		else:
			op = "-"
			ind = pattern.find("-")

		first = int(numbers[:ind])
		second = int(numbers[ind:])

		if op == "+":
			print(first + second)
		else:
			print(first - second)