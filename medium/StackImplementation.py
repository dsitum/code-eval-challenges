#!/usr/bin/env python3

import sys
from collections import deque

with open(sys.argv[1], "r") as f:
	for line in f:
		numbers = line.rstrip().split()
		stack = deque()
		output = ""

		for n in numbers:
			stack.append(n)

		printNumber = True
		while len(stack) > 0:
			if printNumber:
				output += stack.pop() + " "
			else:
				stack.pop()

			printNumber = not printNumber

		print(output[:-1])
