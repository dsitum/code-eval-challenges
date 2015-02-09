#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	board = [[0 for i in range(256)] for j in range(256)]

	for line in f:
		line = line.strip().split()

		if len(line) == 3:
			command, rowcol, value = line
			rowcol = int(rowcol)
			value = int(value)
		else:
			command, rowcol = line
			rowcol = int(rowcol)


		if (command == "SetRow"):
			board[rowcol] = [value for i in range(256)]
		elif (command == "SetCol"):
			board = list(zip(*board))
			board[rowcol] = [value for i in range(256)]
			board = list(zip(*board))
		elif (command == "QueryRow"):
			print(sum(board[rowcol]))
		elif (command == "QueryCol"):
			board = list(zip(*board))
			print(sum(board[rowcol]))
			board = list(zip(*board))