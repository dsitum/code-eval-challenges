#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		n = int(line)
		sum = 0

		while (n > 0):
			sum += n % 10
			n = int(n / 10)

		print(sum)