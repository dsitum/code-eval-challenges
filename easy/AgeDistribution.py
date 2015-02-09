#!/usr/bin/env python3

import sys

def ageDist(age):
	if age in range(0, 3):
		return "Still in Mama's arms"
	if age in range(3, 5):
		return "Preschool Maniac"
	if age in range(5, 12):
		return "Elementary school"
	if age in range(12, 15):
		return "Middle school"
	if age in range(15, 19):
		return "High school"
	if age in range(19, 23):
		return "College"
	if age in range(23, 66):
		return "Working for the man"
	if age in range(66, 101):
		return "The Golden Years"

	return "This program is for humans"

with open(sys.argv[1], "r") as f:
	for line in f:
		print(ageDist(int(line.rstrip())))
