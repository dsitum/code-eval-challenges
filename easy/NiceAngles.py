#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		angle = float(line.rstrip())

		deg = int(angle)
		min = int((angle - deg) * 60)
		sec = int((angle - deg - min/60) * 3600)

		print("{0}.{1:02d}'{2:02d}\"".format(deg, min, sec))
