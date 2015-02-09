#!/usr/bin/env python3

import sys
import collections

with open(sys.argv[1], "r") as f:
	for line in f:
		elements = line.rstrip().split(",")
		totalElementsHalf = len(elements) / 2

		elementsCounter = collections.Counter(elements)

		major = None
		for e in elementsCounter:
			if elementsCounter[e] > totalElementsHalf:
				major = e
				break

		print(major)
