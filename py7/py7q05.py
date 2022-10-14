#!/usr/bin/env python3
import re

with open('Python_07.fasta','r') as fa:
	fasta = fa.read()
	for gene in re.finditer('>(\S+)\s*(.*)\n([ATCG\n]+)',fasta):
		geneid = gene.group(1)
		description = gene.group(2)
		sequence = gene.group(3)
		print(f'gene id:\t{geneid}\ndescription:\t{description}\nsequence:\n{sequence}')

