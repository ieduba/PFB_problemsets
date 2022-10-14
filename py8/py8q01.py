#!/usr/bin/env python3
import re

infile = input("input file path: ")

with open(infile,'r') as file:
	fasta = file.read()
	
	seqs = {}
	for gene in re.finditer('>(\S*)[ \r\t]*(.*)\n([ATCG\n]+)',fasta):
		seqs[gene.group(1)] = {}
		sequence = gene.group(3)
		unique_seq = set(sequence)
		unique_seq.remove('\n')
	
		for nt in unique_seq:
			seqs[gene.group(1)][nt] = sequence.count(nt)
		
print('gene_ID\tA_count\tT_count\tG_count\tC_count')
for key in seqs:
	print(f"{key}\t{seqs[key]['A']}\t{seqs[key]['T']}\t{seqs[key]['G']}\t{seqs[key]['C']}")

#does not work if not all nts are present
