#!/usr/bin/env python3

import sys
import math

with open(sys.argv[1], "r") as f:
	for line in f:
		n = line.rstrip()
		e = len(n)
		sum = 0

		for c in n:
			sum += math.pow(int(c), e)

		if (sum == int(n)):
			print("True")
		else:
			print("False")