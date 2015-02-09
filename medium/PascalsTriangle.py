#!/usr/bin/env python3

from sys import argv

with open(argv[1], "r") as f:
	for line in f:
		levels = int(line.rstrip())

		triangle = [ [1] ]

		for i in range(1, levels):
			row = []

			for j in range(i+1):
				if j == 0 or j == i:
					row.append(1)
				else:
					row.append(triangle[i-1][j-1] + triangle[i-1][j])

			triangle.append(row)


		print(" ".join(str(n) for row in triangle for n in row))
