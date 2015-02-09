#!/usr/bin/env python3

from string import ascii_uppercase

cypherText = (("012222"), ("1114142503"), ("03141418192102"), ("0113"), ("2419182119021713"), ("06131715070119"))
key = "BHISOECRTMGWYVALUZDNFJKPQX"
alpha = ascii_uppercase

plain = ""
for word in cypherText:
	for i in range(0, len(word), 2):
		plain += alpha[key.index(alpha[int(word[i:i+2])])]
	plain += " "

print(plain[:-1])
