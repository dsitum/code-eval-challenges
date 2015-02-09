#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		line = line.rstrip()

		upper = True
		for c in line:
			if c.isalpha():
				if upper:
					print(c.upper(), end="")
				else:
					print(c.lower(), end="")
				upper = not upper
			else:
				print(c, end="")

		print()
