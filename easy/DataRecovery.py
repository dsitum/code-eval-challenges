#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		text, positions = line.rstrip().split(";")
		text = text.split()
		positions = [int(n) for n in positions.split()]

		if len(positions) < len(text):
			for i in range(1, len(text)+1):
				if not i in positions:
					positions.append(i)
					break

		sortedText = [t for (p, t) in sorted(zip(positions, text))]
		print(" ".join(sortedText))