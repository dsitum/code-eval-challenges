#!/usr/bin/env python3

from sys import argv

with open(argv[1], "r") as f:
	for line in f:
		a, b = line.rstrip().split(",")
		if a.endswith(b):
			print(1)
		else:
			print(0)
