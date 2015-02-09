#!/usr/bin/env python3

import sys
import collections

with open(sys.argv[1], "r") as f:
	for line in f:
		line = [c.lower() for c in line if c.isalpha()]
		counter = collections.Counter(line)
		
		beautyOfLetter = 26
		beautyOfString = 0

		for i in counter.most_common():
			beautyOfString += i[1] * beautyOfLetter
			beautyOfLetter -= 1

		print(beautyOfString)