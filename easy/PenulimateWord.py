#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		words = line.strip().split()
		if len(words) > 1:
			print(words[-2])