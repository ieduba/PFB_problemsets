#!/usr/bin/env python3
import sys
import re

infile = sys.argv[1]

translation_table = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'TAT':'Y', 'TAC':'Y',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}

with open(infile,'r') as file, open('Python_08.codons-6frames.nt','w') as writecodons, open('Python_08.translated.aa','w') as writeaas:
	fasta = file.read()
	
	seqs = {}
	for gene in re.finditer('>(\S*)\s*(.*)\n([ATCG\n]+)',fasta):
		seqs[gene.group(1)] = {}
		sequence = gene.group(3).replace('\n','')
		comp = sequence.replace('A','t').replace('T','a').replace('C','g').replace('G','c').upper()
		rc = comp[::-1]
		for i in range(3):	
			seqs[gene.group(1)][f'frame{i+1}'] = re.findall('([ATCG]{3})', sequence[i:])
			seqs[gene.group(1)][f'frame{i+1}rc'] = re.findall('([ATCG]{3})', rc[i:])

	aas = {}
	for gene in seqs:
		aas[gene] = {}
		for frame in seqs[gene]:
			aas[gene][frame] = []
			for codon in seqs[gene][frame]:
				aas[gene][frame].append(translation_table[codon])
	
	for gene in seqs:
		for frame in seqs[gene]:
			writecodons.write(f'{gene}-{frame}-codons\n{seqs[gene][frame]}\n')
			writeaas.write(f'{gene}-{frame}-AAs\n{aas[gene][frame]}\n')
