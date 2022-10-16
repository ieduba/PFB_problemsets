#!/usr/bin/env python3
import sys
import re

def format_dna(dna,linelen):
	dna = dna.replace('\n','')
	startpos = 0
	endpos = linelen
	lines = []
	go = True
	while go == True:
		if endpos == len(dna):
			go = False
		lines.append(dna[startpos:endpos])
		startpos = endpos
		endpos += linelen
		if endpos > len(dna):
			endpos = len(dna)
	newdna = ('\n').join(lines)
	return newdna

def gc_content(dna):
	dna = dna.replace('\n','')
	nGC = dna.count('G') + dna.count('C')
	gc = nGC / len(dna)
	return gc

def reverse_complement(dna):
	dna = dna.replace('\n','')
	comp = dna.replace('A','t').replace('T','a').replace('G','c').replace('C','g')
	rc = comp.upper()[::-1]
	return rc

fa_file = sys.argv[1]
linelen = int(sys.argv[2])

with open(fa_file,'r') as fa:
	fasta = fa.read()
	for gene in re.finditer('>(\S*)[ \r\t]*(.*)\n([\w\n]+)',fasta):
		sequence = gene.group(3).replace('\n','')
		formattedseq = format_dna(sequence, linelen)
		#print(f'{gene.group(1)}\t{gene.group(2)}\n{formattedseq}')
		
		percentGC = gc_content(sequence)
		rc_seq = reverse_complement(sequence)
		print(f'{gene.group(1)}\t{gene.group(2)}\nGC content: {percentGC}\nreverse complement:\n{rc_seq}')
