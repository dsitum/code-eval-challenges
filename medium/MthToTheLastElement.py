#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		chars = line.rstrip().split()
		m = int(chars.pop())
		i = len(chars) - m

		if i < 0:
			continue
		else:
			print(chars[i])