#!/usr/bin/env python3

import sys

def sumsq(n):
	ssq = 0
	while (n > 0):
		last = n % 10
		ssq += last * last
		n = int(n / 10)

	return ssq


with open(sys.argv[1], "r") as f:
	for line in f:
		n = int(line)
		sumOfSquareList = []
		while n not in sumOfSquareList:
			sumOfSquareList.append(n)
			n = sumsq(n)
		
		if sumOfSquareList[-1] == 1:
			print("1")
		else:
			print("0")