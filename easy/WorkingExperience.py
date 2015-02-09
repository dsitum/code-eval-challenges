#!/usr/bin/env python3

import sys
import re

months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

with open(sys.argv[1], "r") as f:
	for line in f:
		dates = line.rstrip().split("; ")
		workMonths = {y :[False for m in range(12)] for y in range(1990, 2021)}
		monthsWorked = 0

		for dateRange in dates:
			m1, y1, m2, y2 = re.findall(r"\w+", dateRange)
			m1 = months.index(m1)
			m2 = months.index(m2)
			y1 = int(y1)
			y2 = int(y2)

			for i in range(y1, y2+1):
				startingMonth = m1 if i == y1 else 0
				endingMonth = m2 if i == y2 else 11
				for j in range(startingMonth, endingMonth + 1):
					if workMonths[i][j] == False:
						monthsWorked += 1
						workMonths[i][j] = True

		print(int(monthsWorked / 12))
