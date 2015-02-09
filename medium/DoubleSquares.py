#!/usr/bin/env python3

from sys import argv

with open(argv[1], "r") as f:
	testCases = int(f.readline().rstrip())
	
	for i in range(testCases):
		n = int(f.readline().rstrip())
		
		pairsNum = 0
		pairs = []

		for a in range(int(n**0.5)+1):
			b = (n - a*a)**0.5
			if int(b) == b and a not in pairs:
				pairsNum += 1
				pairs.append(a)
				pairs.append(b)

		print(pairsNum)
