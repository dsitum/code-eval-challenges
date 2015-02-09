#!/usr/bin/env python3

import sys

tree = {
	"30": {
		"8": {
			"3": None,
			"20": {
				"10": None,
				"29": None
			}
		},
		"52": None
	}
}

commonAncestor = None


def hasChild(tree, child):
	if tree is None:
		return False

	for k in tree:
		if k == child:
			return True
		else:
			if hasChild(tree[k], child):
				return True

	return False


def findCommonAncestor(tree, n1, n2):
	global commonAncestor

	for k in tree:
		if hasChild(tree[k], n1) and hasChild(tree[k], n2) or \
			k == n1 and hasChild(tree[k], n2) or \
			k == n2 and hasChild(tree[k], n1):
				commonAncestor = k
				findCommonAncestor(tree[k], n1, n2)
				break

	return commonAncestor


with open(sys.argv[1], "r") as f:
	for line in f:
		n1, n2 = line.rstrip().split()
		commonAncestor = findCommonAncestor(tree, n1, n2)
		
		if commonAncestor is not None:
			print(commonAncestor)
