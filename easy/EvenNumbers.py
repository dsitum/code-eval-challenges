#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		number = int(line.rstrip())
		print(1 - number % 2)
