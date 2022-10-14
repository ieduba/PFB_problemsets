#!/usr/bin/env python3
import sys
import re

infile = sys.argv[1]

with open(infile,'r') as file, open('Python_08.codons-6frames.nt','w') as writefile:
	fasta = file.read()
	
	seqs = {}
	for gene in re.finditer('>(\S*)\s*(.*)\n([ATCG\n]+)',fasta):
		seqs[gene.group(1)] = {}
		sequence = gene.group(3).replace('\n','')
		comp = sequence.replace('A','t').replace('T','a').replace('C','g').replace('G','c').upper()
		rc = comp[::-1]	
		seqs[gene.group(1)]['frame1'] = re.findall('([ATCG]{3})', sequence)
		seqs[gene.group(1)]['frame2'] = re.findall('([ATCG]{3})', sequence[1:])
		seqs[gene.group(1)]['frame3'] = re.findall('([ATCG]{3})', sequence[2:])
		seqs[gene.group(1)]['frame1rc'] = re.findall('([ATCG]{3})', rc)
		seqs[gene.group(1)]['frame2rc'] = re.findall('([ATCG]{3})', rc[1:])
		seqs[gene.group(1)]['frame3rc'] = re.findall('([ATCG]{3})', rc[2:])
	for key in seqs:
		writefile.write(f'{key}-frame1-codons\n{seqs[key]["frame1"]}\n')
		writefile.write(f'{key}-frame2-codons\n{seqs[key]["frame2"]}\n')
		writefile.write(f'{key}-frame3-codons\n{seqs[key]["frame3"]}\n')
		writefile.write(f'{key}-frame1rc-codons\n{seqs[key]["frame1rc"]}\n')
		writefile.write(f'{key}-frame2rc-codons\n{seqs[key]["frame2rc"]}\n')
		writefile.write(f'{key}-frame3rc-codons\n{seqs[key]["frame3rc"]}\n')
