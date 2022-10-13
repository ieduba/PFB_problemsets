#!/usr/bin/env python3
with open('Python_06.seq.txt','r') as seq_file, open('Python_06_rc.seq.txt','w') as rc_file:
	for line in seq_file:
		name,seq = line.rstrip().split()
		comp = seq.replace('A','t').replace('T','a').replace('C','g').replace('G','c').upper()
		rc = comp[::-1]
		rc_file.write(f'{name}\t{rc}\n')
