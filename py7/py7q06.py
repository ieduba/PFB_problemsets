#!/usr/bin/env python3
import re

with open('Python_07_ApoI.fasta','r') as file:
	fasta = file.read()
	sequence = re.sub('>\S+[ \r\t]*.*','',fasta).replace('\n','')
	cutseq = sequence
	print('cut sites and positions:')
	for site in re.finditer('[AG]AATT[CT]', sequence):
		siteseq = site.group()
		cutsiteseq = siteseq.replace('AAT','^AAT')
		pos = site.start()
		print(f'position: {pos}\tsite: {cutsiteseq}')
		cutseq = re.sub(siteseq, cutsiteseq, cutseq)
print(f'\nwhole sequence with cut sites:\n{cutseq}\n')

frags = sorted(cutseq.split('^'), key = len, reverse = True)
print('resulting fragments on gel:')
for frag in frags:
	print(f'frag: {frag}\tlength: {len(frag)} bp')

