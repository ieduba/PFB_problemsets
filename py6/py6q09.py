#!/usr/bin/env python3

with open('Python_06.fasta','r') as fa:
	names = []
	seqs = []
	for line in fa:
		line = line.rstrip()
		if line[0] == '>':
			line = line[1:]
			names.append(line)
		else:
			seqs.append(line)
	
	seqdic = {}
	for i in range(len(names)):
		seqdic[names[i]] = seqs[i]

print(seqdic)
