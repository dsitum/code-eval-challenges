#!/usr/bin/env python3

import sys

raceWay = []

with open(sys.argv[1], "r") as f:
	for line in f:
		raceWay.append(line.rstrip())

exPassIndex = None

for i,e in enumerate(raceWay):
	passChar = "C"
	passIndex = e.find("C")

	if passIndex == -1:
		passIndex = e.find("_")
		passChar = "_"

	if i == 0 or exPassIndex == passIndex:
		turn = "|"
	elif exPassIndex < passIndex:
		turn = "\\"
	else:
		turn = "/"

	print(e.replace(passChar, turn))

	exPassIndex = passIndex