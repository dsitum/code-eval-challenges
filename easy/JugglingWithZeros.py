#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		zeros = line.rstrip().split()

		n = ""
		
		for i in range(0, len(zeros), 2):
			if zeros[i] == "0":
				c = "0"
			else:
				c = "1"

			for z in zeros[i+1]:
				n += c

		print(int(n, 2))