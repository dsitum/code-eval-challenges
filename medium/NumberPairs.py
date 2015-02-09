#!/usr/bin/env python3

from sys import argv

with open(argv[1], "r") as f:
	for line in f:
		if line.rstrip() == "":
			break

		numbers, x = line.rstrip().split(";")
		numbers = [int(i) for i in numbers.split(",")]
		x = int(x)
		n = len(numbers)
		pairs = []

		for i in range(n):
			for j in range(i+1, n):
				if numbers[i] + numbers[j] == x:
					pairs.append((str(numbers[i]),str(numbers[j])))

		if len(pairs) == 0:
			print("NULL")
		else:
			print(";".join(",".join(pair) for pair in pairs))
