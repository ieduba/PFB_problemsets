#!/usr/bin/env python3

import sys
import re

with open(sys.argv[1],'r') as samfile:
	readgenepairs = set()
	for line in samfile:
		found = re.search('([_\d]+)\s+\d+\s+([\w_-]+)', line)
		read = found.group(1)
		gene = found.group(2)
		readgenepairs.add((read,gene))

readcounts = {}
for pair in readgenepairs:
	uniquegene = pair[1]
	if uniquegene not in readcounts:
		readcounts[uniquegene] = 1
	else:
		readcounts[uniquegene] += 1

sortedkeys = [sorted(readcounts.items(), key = lambda pair: pair[1], reverse = True)[i][0] for i in range(len(readcounts))]

print('gene\tN reads')
for key in sortedkeys[:14]:
	print(f'{key}\t{readcounts[key]}')
