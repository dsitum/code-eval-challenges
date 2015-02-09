#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		words = line.rstrip().split()
		n = len(words)
		output = ""

		for word in words:
			output += word[0].capitalize() + word[1:] + " "

		print(output[:-1])