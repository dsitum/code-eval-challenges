#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		words = line.rstrip().split(";")

		for word in words:
			if (word == "zero"):
				print(0, end="")
			if (word == "one"):
				print(1, end="")
			if (word == "two"):
				print(2, end="")
			if (word == "three"):
				print(3, end="")
			if (word == "four"):
				print(4, end="")
			if (word == "five"):
				print(5, end="")
			if (word == "six"):
				print(6, end="")
			if (word == "seven"):
				print(7, end="")
			if (word == "eight"):
				print(8, end="")
			if (word == "nine"):
				print(9, end="")

		print()