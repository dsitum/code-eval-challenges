#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		sentence = line.rstrip().split()
		longestWord = ""

		for word in sentence:
			if len(word) > len(longestWord):
				longestWord = word

		print(longestWord)