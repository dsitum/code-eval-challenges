#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		chars, seq = line.rstrip().split("|")
		seq = [int(x) for x in seq.split()]

		for n in seq:
			print(chars[n-1], end="")

		print()