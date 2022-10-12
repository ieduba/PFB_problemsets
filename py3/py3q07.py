#!/usr/bin/env python3
import sys

dna = sys.argv[1]

rna = dna.replace('T','U')
rna = rna.replace('t','u')

print(rna)
