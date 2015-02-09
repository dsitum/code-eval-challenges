#!/usr/bin/env python3

from sys import argv
from string import ascii_lowercase

with open(argv[1], "r") as f:
	for line in f:
		usedChars = set(c for c in line.rstrip().lower())
		allChars = set(ascii_lowercase)

		unused = allChars - usedChars
		unusedChars = sorted(list(unused))

		if (len(unusedChars) == 0):
			print("NULL")
		else:
			print("".join(unusedChars))
