#!/usr/bin/env python3
import sys

file = sys.argv[1]
qthresh = int(sys.argv[2])

with open(file, 'r') as fastq:
	linecount = 0
	cutoffs = {}
	for line in fastq:
		line = line.rstrip()
		if linecount%4 == 3:
			for scorei in range(len(line)-1,-1,-1):
				if (ord(line[scorei]) - 33) > qthresh:
					cutoffs[linecount] = scorei
					break
		linecount += 1
	
with open(file, 'r') as fastq, open(f'trimmed-{file}', 'w') as trimmed:
	linecount = 0
	for line in fastq:
		line = line.rstrip()
		if linecount%4 == 0:
			trimmed.write(f'{line}\n')
		elif linecount%4 == 1:
			trimmedline = line[0:cutoffs[linecount + 2]]
			trimmed.write(f'{trimmedline}\n')
		elif linecount%4 == 2:
			trimmed.write(f'{line}\n')
		elif linecount%4 == 3:
			trimmedline = line[0:cutoffs[linecount]]
			trimmed.write(f'{trimmedline}\n')
		linecount += 1
