#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		x, n = [int(nr) for nr in line.rstrip().split(",")]
		multiple = n
		
		while multiple < x:
			multiple += n

		print(multiple)