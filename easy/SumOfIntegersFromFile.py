#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	sum = 0
	for line in f:
		sum += int(line)

	print(sum)