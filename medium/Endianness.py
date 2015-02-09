#!/usr/bin/env python3

from sys import byteorder

if byteorder == "little":
	print("LittleEndian")
else:
	print("BigEndian")
