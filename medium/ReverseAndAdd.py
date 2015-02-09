#!/usr/bin/env python3

from sys import argv

with open(argv[1], "r") as f:
	for line in f:
		n = int(line.rstrip())

		for i in range(1, 101):
			n += int(str(n)[::-1])
			if n == int(str(n)[::-1]):
				print(i, n)
				break
