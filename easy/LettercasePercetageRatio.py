#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		line = line.rstrip()
		upper = 0
		lower = 0

		for c in line:
			if c.isupper():
				upper += 1
			else:
				lower += 1

		upperPercent = upper / (upper + lower) * 100
		lowerPercent = lower / (upper + lower) * 100

		print("lowercase: {0:.2f} uppercase: {1:.2f}".format(lowerPercent, upperPercent))