#!/usr/bin/env python3

import sys

def toSeconds(l):
	return int(l[0])*3600 + int(l[1])*60 + int(l[2])

with open(sys.argv[1], "r") as f:
	for line in f:
		t1, t2 = [t.split(":") for t in line.rstrip().split()]
		t1 = toSeconds(t1)
		t2 = toSeconds(t2)

		diff = abs(t1 - t2)
		h = int(diff/3600)
		m = int((diff - h*3600) / 60)
		s = diff - h*3600 - m*60

		print("{0:02d}:{1:02d}:{2:02d}".format(h,m,s))
