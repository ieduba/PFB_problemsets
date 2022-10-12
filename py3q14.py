#!/usr/bin/env python3
import sys

dna = sys.argv[1]
ecoRI = 'GAATTC'

sitestart = dna.find(ecoRI) + 1
siteend = sitestart + len(ecoRI) - 1

print(f'EcoRI startPos: {sitestart} endPos: {siteend}')
