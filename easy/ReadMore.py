#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		line = line.rstrip()
		if len(line) <= 55:
			print(line)
		else:
			line = line[:40]
			if line.rfind(" ") != -1:
				print("{0}... <Read More>".format(line[:line.rfind(" ")].rstrip()))
			else:
				print("{0}... <Read More>".format(line))
