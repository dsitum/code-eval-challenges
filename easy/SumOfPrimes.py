#!/usr/bin/env python3

import math

sum = 2
n = 3
found = 1

while found < 1000:
	prime = True
	if n % 2 == 1:
		for i in range(2, int(math.sqrt(n))+1):
			if n % i == 0:
				prime = False
				continue
		if prime:
			sum += n
			found += 1

	n += 1

print(sum)