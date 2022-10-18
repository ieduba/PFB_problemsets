#!/usr/bin/env python3
from Bio import SeqIO
import sys

def gc_content(dna):
	dna = dna.replace('\n','')
	nGC = dna.count('G') + dna.count('C')
	gc = nGC / len(dna)
	return gc

file = sys.argv[1]

lens = []
gcs = []
for seq_record in SeqIO.parse(file, 'fasta'):
	#print(f'sequence name: {seq_record.id}\ndescription: {seq_record.description}\nsequence: {seq_record.seq}')
	lens.append(len(seq_record))
	gcs.append(gc_content(str(seq_record.seq)))
print(f'''number sequences: {len(lens)}
number of nucleotides: {sum(lens)}
average seq length: {sum(lens)/len(lens):.4f}
shortest seq length: {min(lens)}
longest seq length: {max(lens)}
average GC content: {sum(gcs)/len(gcs):.4f}
max GC content: {max(gcs):.4f}
min GC content: {min(gcs):.4f}
''')
