#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		mixed = line.rstrip().split(",")
		words = []
		digits = []

		for content in mixed:
			if content.isdigit():
				digits.append(content)
			else:
				words.append(content)

		if (len(words) == 0):
			print(",".join(digits))
		elif (len(digits) == 0):
			print(",".join(words))
		else:
			print(",".join(words) + "|" + ",".join(digits))