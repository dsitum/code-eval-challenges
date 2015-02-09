#!/usr/bin/env python3

import sys
import collections

def toRoman(digit, unit):
	romanValues = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}

	number = digit * unit
	keys = sorted(list(romanValues.keys()))
	i = keys.index(unit)

	if digit == 0:
		return ""
	elif digit == 1 or digit == 5:
		return romanValues[number]
	elif digit == 4:
		return romanValues[keys[i]] + romanValues[keys[i+1]]
	elif digit == 9:
		return romanValues[keys[i]] + romanValues[keys[i+2]]
	elif digit == 2 or digit == 3:
		return digit * romanValues[keys[i]]
	else:  # digit is 6, 7 or 8
		return romanValues[keys[i+1]] + (digit - 5) * romanValues[keys[i]]


			

with open(sys.argv[1], "r") as f:
	for line in f:
		number = int(line.rstrip())
		romanNumberParts = collections.deque()
		unit = 1

		while (number > 0):
			lastDigit = number % 10
			romanPart = toRoman(lastDigit, unit)
			romanNumberParts.append(romanPart)

			number = int(number / 10)
			unit *= 10

		print("".join(reversed(romanNumberParts)))
