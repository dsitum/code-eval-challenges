#!/usr/bin/env python3

import sys

def morseToChar(code):
	if code == ".-":
		return "A"
	if code == "-...":
		return "B"
	if code == "-.-.":
		return "C"
	if code == "-..":
		return "D"
	if code == ".":
		return "E"
	if code == "..-.":
		return "F"
	if code == "--.":
		return "G"
	if code == "....":
		return "H"
	if code == "..":
		return "I"
	if code == ".---":
		return "J"
	if code == "-.-":
		return "K"
	if code == ".-..":
		return "L"
	if code == "--":
		return "M"
	if code == "-.":
		return "N"
	if code == "---":
		return "O"
	if code == ".--.":
		return "P"
	if code == "--.-":
		return "Q"
	if code == ".-.":
		return "R"
	if code == "...":
		return "S"
	if code == "-":
		return "T"
	if code == "..-":
		return "U"
	if code == "...-":
		return "V"
	if code == ".--":
		return "W"
	if code == "-..-":
		return "X"
	if code == "-.--":
		return "Y"
	if code == "--..":
		return "Z"
	if code == "-----":
		return "0"
	if code == ".----":
		return "1"
	if code == "..---":
		return "2"
	if code == "...--":
		return "3"
	if code == "....-":
		return "4"
	if code == ".....":
		return "5"
	if code == "-....":
		return "6"
	if code == "--...":
		return "7"
	if code == "---..":
		return "8"
	if code == "----.":
		return "9"
	if code == "SP":
		return " "

with open(sys.argv[1], "r") as f:
	for line in f:
		morseChars = line.rstrip().replace("  ", " SP ").split()

		for c in morseChars:
			print(morseToChar(c), end="")

		print()