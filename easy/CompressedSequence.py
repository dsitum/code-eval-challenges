#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		seq = line.rstrip().split()
		
		compressed = []
		last = seq[0]
		reps = 0

		for n in seq:
			if n == last:
				reps += 1
			else:
				compressed.append(str(reps))
				compressed.append(last)
				last = n
				reps = 1

		compressed.append(str(reps))
		compressed.append(last)

		print(" ".join(compressed))