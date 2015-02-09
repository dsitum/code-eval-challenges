#!/usr/bin/env python3

import sys

def contains(number, times, listOfNumbers):
	testTimes = 0
	for n in listOfNumbers:
		if number == n:
			testTimes += 1

	if testTimes == times:
		return True
	else:
		return False



with open(sys.argv[1], "r") as f:
	for line in f:
		numbers = [int(c) for c in line.rstrip()]

		selfDescribing = True
		for i,n in enumerate(numbers):
			if not contains(i, n, numbers):
				selfDescribing = False

		if selfDescribing:
			print("1")
		else:
			print("0")
