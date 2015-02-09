#!/usr/bin/env python3

from sys import argv
from collections import OrderedDict

with open(argv[1], "r") as f:
	for line in f:
		line = line.rstrip()
		repetitions = OrderedDict()

		for c in line:
			if c not in repetitions:
				repetitions[c] = 1
			else:
				repetitions[c] += 1

		for c in repetitions:
			if repetitions[c] == 1:
				print(c)
				break
