#!/usr/bin/env python3

seqs = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

#for seq in seqs:
#	print(len(seq),seq,sep='\t')

tup_list = [(len(seq),seq) for seq in seqs]
for tup in tup_list:
	print(tup_list.index(tup),tup[0],tup[1],sep='\t')

