#!/usr/bin/env python3

import sys
import re
import math

with open(sys.argv[1], "r") as f:
	for line in f:
		numbers = [int(x) for x in re.findall(r"\d+|-\d+", line.rstrip())]

		d = math.sqrt((numbers[0] - numbers[2])**2 + (numbers[1] - numbers[3])**2)
		print(int(d))