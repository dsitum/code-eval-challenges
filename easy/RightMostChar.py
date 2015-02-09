#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		line = line.rstrip("\n").split(",")
		text = line[0]
		char = line[1][0]

		if char in text:
			print(len(text) - text[::-1].index(char) - 1)
		else:
			print("-1")