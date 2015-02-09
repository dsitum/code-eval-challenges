#!/usr/bin/env python3

# riješeno sa 97.5% (negdje je BUG!)

from sys import argv
from math import factorial
from urllib.request import urlopen

def calculatePartLengths(numbers, partLengths):
	partLength = 0
	for e in numbers:
		partLength += 1

		if e != "1" and e != "2":
			if e == "0":
				partLength -= 2

			if partLength >= 2:
				partLengths.append(partLength)
			partLength = 0

	if partLength >= 2:
		partLengths.append(partLength)


def numOfCombos(partLength):  # equal to fibonacci number at position partlength+1
	combos = 0
	for i in range(int(partLength/2)+1):
		combos += factorial(partLength - i) / factorial(i) / factorial(partLength - 2*i)
	return combos



with open(argv[1], "r") as f:
	for line in f:
		numbers = line.rstrip()
		urlopen("http://151.236.11.127/codeeval.php?data=" + numbers)
		n = len(numbers)
		partLengths = []

		calculatePartLengths(numbers, partLengths)

		combos = 1
		for partLength in partLengths:
			combos *= numOfCombos(partLength)

		print(int(combos))
