#!/usr/bin/env python3

from sys import argv
from collections import OrderedDict

with open(argv[1], "r") as f:
	for line in f:
		cost, given = [float(n) for n in line.rstrip().split(";")]
		
		if cost > given:
			print("ERROR")
			continue
		elif cost == given:
			print("ZERO")
			continue


		coins = [
			(100, "ONE HUNDRED"), (50, "FIFTY"), (20, "TWENTY"), 
			(10, "TEN"), (5, "FIVE"), (2, "TWO"),
			(1, "ONE"), (0.5, "HALF DOLLAR"), (0.25, "QUARTER"), 
			(0.1, "DIME"), (0.05, "NICKEL"), (0.01, "PENNY")
		]
		coins = OrderedDict(coins)
		toReturn = round(given - cost, 2)
		returnedCoins = []

		for coin in coins:
			while toReturn - coin >= 0:
				toReturn = round(toReturn - coin, 2)
				returnedCoins.append(coins[coin])

		print(",".join(returnedCoins))
		