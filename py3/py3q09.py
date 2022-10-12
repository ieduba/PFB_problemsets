#!/usr/bin/env python3
import sys

dna = sys.argv[1]
len_dna = len(dna)
nA = dna.count('A')
nT = dna.count('T')
nAT = nA + nT

at_cont = nAT / len_dna
gc_cont = 1 - at_cont

print(f'AT content: {at_cont}')
print(f'GC content: {gc_cont}')
