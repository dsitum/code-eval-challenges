#!/usr/bin/env python3

from sys import argv

with open(argv[1], "r") as f:
	for line in f:
		line = line.rstrip()
		out = ""

		lastChar = ""
		for c in line:
			if c != lastChar:
				out += c
				lastChar = c

		print(out)
