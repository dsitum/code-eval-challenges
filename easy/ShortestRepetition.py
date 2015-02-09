#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		s = line.rstrip()
		period = []

		for i,c in enumerate(s):
			if not c in period:
				period.append(c)
			else:
				for j in range(i+1, len(s)):
					if not s[j] in period:
						period.append(c)
						break

		print(len(period))
