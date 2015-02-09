#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		previous = ''

		for c in line.rstrip().split(","):
			if c != previous:
				if previous != '':
					print(",", end="")

				print(c, end="")
				previous = c

		print()