#!/usr/bin/env python3
import sys

dna = sys.argv[1]

unique = set(dna)
nt_comp = {}
for nt in unique:
	nt_comp[nt] = dna.count(nt)
gc_cont = (nt_comp['G'] + nt_comp['C'])/len(dna)
print(f'counts: {nt_comp}\nGC content: {gc_cont}')
