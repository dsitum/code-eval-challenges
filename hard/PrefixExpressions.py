#!/usr/bin/env python3

from sys import argv
from collections import deque

with open(argv[1], "r") as f:
	for line in f:
		parts = reversed(line.rstrip().split())
		stack = deque()

		for p in parts:
			if p.isdigit():
				stack.append(float(p))
			else:
				if p == "+":
					stack.append(stack.pop() + stack.pop())
				elif p == "*":
					stack.append(stack.pop() * stack.pop())
				elif p == "/":
					stack.append(float(stack.pop() / stack.pop()))

		
		print(int(stack.pop()))
