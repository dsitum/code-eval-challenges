#!/usr/bin/env python3

import sys
import collections

with open(sys.argv[1], "r") as f:
	for line in f:
		l1, l2 = [n.split() for n in line.rstrip().split("|")]
		result = collections.deque()

		for i in range(len(l1)):
			result.append(str(int(l1[i]) * int(l2[i])))

		print(" ".join(result))
		