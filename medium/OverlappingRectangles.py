#!/usr/bin/env python3

from sys import argv

class Rectangle:
	def __init__(self, coords, pos):
		if pos == 1:
			rect = coords[:4]
		else:
			rect = coords[4:]

		self.x1 = rect[0]
		self.y1 = rect[1]
		self.x2 = rect[2]
		self.y2 = rect[3]

	def overlapsWith(self, rect):
		if (self.x1 <= rect.x1 <= self.x2) or (self.x1 <= rect.x2 <= self.x2):
			if (self.y1 >= rect.y2 >= self.y2) or \
				(self.y1 >= rect.y1 >= self.y2) or \
				(rect.y1 >= self.y1 and rect.y2 <= self.y2):
					return True
		return False
	


with open(argv[1], "r") as f:
	for line in f:
		coords = [float(c) for c in line.rstrip().split(",")]
		rect1 = Rectangle(coords, 1)
		rect2 = Rectangle(coords, 2)

		print(rect1.overlapsWith(rect2) or rect2.overlapsWith(rect1))
