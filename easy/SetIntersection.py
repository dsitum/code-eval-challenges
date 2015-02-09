#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		sets = line.rstrip().split(";")
		set1 = sets[0].split(",")
		set2 = sets[1].split(",")

		if len(set2) < len(set1):
			tmp = set1
			set1 = set2
			set2 = tmp


		firstCharacter = True
		for c in set1:
			if c in set2:
				if firstCharacter:
					firstCharacter = False
				else:
					print(",", end="")

				print(c, end="")
				
		print()