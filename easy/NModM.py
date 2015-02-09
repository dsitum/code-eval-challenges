#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		n, m = [int(c) for c in line.rstrip().split(",")]

		while int(n / m) > 0:
			n -= int(n / m) * m

		print(n)