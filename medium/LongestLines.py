#!/usr/bin/env python3

import sys

lines = []

with open(sys.argv[1], "r") as f:
	n = int(f.readline().rstrip())
	for line in f:
		lines.append(line.rstrip())


lines.sort(key=lambda x: len(x), reverse=True)
for i in range(n):
	print(lines[i])
