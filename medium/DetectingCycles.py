#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		mainSeq = line.rstrip().split()
		l = len(mainSeq)
		sequences = []
		repeatingSeq = []

		while True:  # do while, kind of
			for i in range(l):
				for j in range(i, l):
					s = mainSeq[i:j+1]
					if s not in sequences:
						sequences.append(s)
					else:
						if len(s) > len(repeatingSeq):
							repeatingSeq = s
							

			if len(repeatingSeq) == 0:
				break
			else:
				mainSeq = repeatingSeq
				l = len(repeatingSeq)
				sequences = []
				repeatingSeq = []


		print(" ".join(mainSeq))
