#!/usr/bin/env python3

from sys import argv
import re

with open(argv[1], "r") as f:
	for line in f:
		mail = line.strip()
		if mail == "":
			break

		if re.search(r"^[/#$!&a-z0-9._%+-]+@[a-z0-9._-]+\.[a-z]+$", mail, re.IGNORECASE):
			print("true")
		else:
			print("false")
