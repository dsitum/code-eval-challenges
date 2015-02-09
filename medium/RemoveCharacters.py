#!/usr/bin/env python3

from sys import argv

with open(argv[1], "r") as f:
	for line in f:
		text, chars = line.rstrip().split(", ")

		toWrite = [c for c in text if c not in chars]

		print("".join(toWrite))
