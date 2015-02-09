#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		n, p1, p2 = [int(nr) for nr in line.rstrip().split(",")]
		b1 = n >> p1 - 1 & 1
		b2 = n >> p2 - 1 & 1

		if b1 == b2:
			print("true")
		else:
			print("false")