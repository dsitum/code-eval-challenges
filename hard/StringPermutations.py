#!/usr/bin/env python3

import sys

class Permutation:
	def __init__(self, seq):
		self.firstP = sorted([c for c in seq])
		self.nuberOfPermutationsDone = 0

		self.nextP = None



	def hasNextCharacter(self):
		tmpNextP = self.nextP[:]
		self.unusedCharacters = [c for c in self.firstP if not c in tmpNextP or tmpNextP.remove(c)]

		if self.unusedCharacters == []:
			return False

		for elem in self.unusedCharacters:
			if elem >= self.nextP[-1]:
				return True

		return False


	def completeNextPermutation(self):
		for elem in self.unusedCharacters:
			if elem >= self.nextP[-1]:
				removedCharacter = self.nextP.pop()
				self.nextP.append(elem)
				self.unusedCharacters.remove(elem)
				break

		self.unusedCharacters.append(removedCharacter)
		self.unusedCharacters.sort()

		for elem in self.unusedCharacters:
			self.nextP.append(elem)


	def nTotal(self):
		fact = 1
		for i in range(1, len(self.firstP)+1):
			fact *= i
		return fact


	def next(self):
		if self.nuberOfPermutationsDone == self.nTotal():
			return False
		else:
			self.nuberOfPermutationsDone += 1

		if self.nextP is None:
			self.nextP = self.firstP[:]
			return "".join(self.nextP)

		self.nextP.pop()
		while (not self.hasNextCharacter()) and (len(self.nextP)) > 0:
			self.nextP.pop()

		self.completeNextPermutation()
		return "".join(self.nextP)



if __name__ == "__main__":
	with open(sys.argv[1], "r") as f:
		for line in f:
			p = Permutation(line.rstrip())

			for i in range(p.nTotal()):
				print(p.next(), end="")
				
				if i < p.nTotal() - 1:
					print(",", end="")
				else:
					print()