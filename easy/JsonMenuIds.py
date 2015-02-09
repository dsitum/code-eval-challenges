#!/usr/bin/env python3

import sys
import json

sum = 0

def sumOfIds(node):
	if type(node) is dict:
		keys = node.keys()
		if "id" in keys and "label" in keys:
				global sum
				sum += int(node["id"])
		for key in keys:
			sumOfIds(node[key])

	elif type(node) is list:
		for elem in node:
			sumOfIds(elem)


with open(sys.argv[1], "r") as f:
	for line in f:
		sum = 0
		jsonObj = json.loads(line.rstrip())
		sumOfIds(jsonObj)
		print(sum)
