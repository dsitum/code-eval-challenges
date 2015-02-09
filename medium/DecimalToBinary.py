#!/usr/bin/env python3

from sys import argv

with open(argv[1], "r") as f:
	for line in f:
		binNum = bin(int(line.rstrip()))[2:]
		print(binNum)
