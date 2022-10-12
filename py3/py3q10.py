#!/usr/bin/env python3
import sys

dna = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])

dna_sub = dna[start-1:end]
ng = dna_sub.count('G') + dna_sub.count('g')

print(f'{dna_sub} contains {ng} Gs')
