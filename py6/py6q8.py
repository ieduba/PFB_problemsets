#!/usr/bin/env python3

with open('Python_06.fastq','r') as fq:
	count = 0
	chars = 0
	for line in fq:
		line = line.rstrip()
		count += 1
		chars += len(line)
print(f'number of lines: {count}\ntotal characters: {chars}\navg line length: {chars/count}')
