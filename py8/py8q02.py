#!/usr/bin/env python3
import sys
import re

infile = sys.argv[1]

with open(infile,'r') as file:
	fasta = file.read()
	
	seqs = {}
	for gene in re.finditer('>(\S*)\s*(.*)\n([ATCG\n]+)',fasta):
		sequence = gene.group(3).replace('\n','')
		seqs[gene.group(1)] = re.findall('([ATCG]{3})', sequence)

for key in seqs:
	print(f'{key}-frame1-codons\n{seqs[key]}\n')
