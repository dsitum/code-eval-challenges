#!/usr/bin/env python3

from sys import argv
from collections import deque

openingP = ("(", "[", "{")
closingP = (")", "]", "}")

with open(argv[1], "r") as f:
	for line in f:
		parentheses = line.rstrip()

		validParentheses = True
		stack = deque()

		for p in parentheses:
			if p in openingP:
				stack.append(p)

			elif p in closingP and len(stack) > 0:
				stackTop = stack.pop()
				leftP = openingP.index(stackTop)
				rightP = closingP.index(p)
				if leftP != rightP:
					validParentheses = False
					break

			else:
				validParentheses = False
				break

		if len(stack) > 0:
			validParentheses = False

		print(validParentheses)
