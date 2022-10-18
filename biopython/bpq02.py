#!/usr/bin/env python3
from Bio import SeqIO
import sys

file = sys.argv[1]

ids = [record.id for record in SeqIO.parse(file,'fasta')]
print(len(ids))

descs = [record.description for record in SeqIO.parse(file,'fasta')]
print(descs[:10])
