#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		distances = [int(d.split(",")[1]) for d in line.rstrip().replace(" ", "")[:-1].split(";")]
		distances.sort()
		travel = []

		travel.append(distances[0])
		for i in range(1, len(distances)):
			travel.append(distances[i] - distances[i-1])

		print(",".join([str(d) for d in travel]))