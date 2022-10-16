#!/usr/bin/env python3
import re
import sys

## create restriction enzyme dictionary
with open('bionet.txt','r') as file:
	lineN = 0
	re_dict = {}
	for line in file:
		lineN += 1
		if lineN <= 10:
			continue
		if line[0] == '\n':
			continue

		found = re.search('(\w+( \(.+\))?)\s+([A-Z\^]+)', line)
		re_name = found.group(1)
		re_site = found.group(3)
		re_dict[re_name] = re_site

## IUPAC code dictionary
code_dict = {'^':'^', 'A':'A', 'T':'T', 'C':'C', 'G':'G', 'R':'[AG]', 'Y':'[CT]', 'S':'[GC]', 'W':'[AT]', 'K':'[GT]', 'M':'[AC]', 'B':'[CGT]', 'D':'[AGT]', 'H':'[ACT]', 'V':'[ACG]', 'N':'[ATCG]'}

## read in inputs -- this does not work :( can't get it to print cut sites 
enzyme = sys.argv[1]
fa = sys.argv[2]
site_raw = re_dict[enzyme]
print(site_raw)
site_tofind = site_raw
for base in site_tofind:
	site_tofind = site_tofind.replace(base, code_dict[base])
site_raw_nocarrot = site_raw.replace('^','')
site_tofind_nocarrot = site_tofind.replace('^','')
print(site_raw_nocarrot)
print(site_tofind_nocarrot)

with open(fa, 'r') as file:
	fasta = file.read()
	sequence = re.sub('>\S+[ \r\t]*.*','',fasta).replace('\n','') #remove header and concatenate lines
	print(sequence)
	seq_wcarrots = re.sub(site_nocarrot, site_tofind, sequence)
	print(seq_wcarrots)
	for site in re.finditer(site_tofind, sequence):
		siteseq = site.group()
		cutsiteseq = siteseq.replace(site_nocarrot, site_tofind)
		cutseq = re.sub(siteseq, cutsiteseq, cutseq)

print(f'\nwhole sequence with cut sites:\n{cutseq}\n')

frags = sorted(cutseq.split('^'), key = len, reverse = True)
print('resulting fragments on gel:')
for frag in frags:
	print(f'frag: {frag}\tlength: {len(frag)} bp')
