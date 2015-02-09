#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		args = line.rstrip().split(":")
		array = args[0].split()
		positions = [r.split("-") for r in args[1].replace(" ", "").split(",")]

		for pos in positions:
			p1 = int(pos[0])
			p2 = int(pos[1])
			tmp = array[p1]
			array[p1] = array[p2]
			array[p2] = tmp

		print(" ".join(array))
