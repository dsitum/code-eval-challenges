#!/usr/bin/env python3

from sys import argv

with open(argv[1], "r") as f:
	for line in f:
		line = line.rstrip()
		if line == "":
			break

		size, array = line.split(";")
		array = array.split(",")

		used = [False for _ in array]

		for e in array:
			e = int(e)
			if used[e] == True:
				print(e)
				break
			else:
				used[e] = True
