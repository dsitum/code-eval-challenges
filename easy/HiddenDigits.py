#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		chars = line.rstrip()
		hiddenDigits = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")
		out = ""

		for c in chars:
			if c.isdigit():
				out += c
			elif c in hiddenDigits:
				out += str(hiddenDigits.index(c))

		if out == "":
			print("NONE")
		else:
			print(out)
