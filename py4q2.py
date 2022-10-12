#!/usr/bin/env python3
import sys

taxa = 'sapiens, erectus, neanderthalensis'
print(taxa[1])
print(type(taxa))

species = taxa.split(', ')
print(species)
print(species[1])
print(type(species))

print(sorted(species))
print(sorted(species,key=len))
