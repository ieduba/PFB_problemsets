#!/usr/bin/env python3
import sys

def parseblast(file):
	with open(file, 'r') as toparse:
		for line in toparse:
			if line[0] == '#':
				continue
			else:
				line = line.rstrip()
				vals = line.split('\t')
				this_data = dict(zip(colnames, vals))
				break
	return this_data

seqlen = sys.argv[1] #rand5-200 or rand5-800
colnames = ['qseqid', 'sseqid', 'percid', 'alen', 'mismat', 'gaps', 'q_start', 'q_end', 's_start', 's_end', 'evalue', 'bits']

print('SSEARCH')
print('s_mat\t%_id\ta_len\tE_val')
all_data = {}
for scoremat in ['BL50', 'BP62', 'VT10', 'VT20', 'VT40', 'VT80', 'VT160']:
	infile = 'ss_' + seqlen + '_v_qfo_' + scoremat + '.txt'
	all_data[scoremat] = parseblast(infile)
	print(f'{scoremat}\t{all_data[scoremat]["percid"]}\t{all_data[scoremat]["alen"]}\t{all_data[scoremat]["evalue"]}')

print('\nBLAST')
print('s_mat\t%_id\ta_len\tE_val')
all_data = {}
for scoremat in ['BLOSUM62', 'BLOSUM80', 'PAM30', 'PAM70']:
	infile = 'blast_' + seqlen + '_v_qfo_' + scoremat + '.txt'
	all_data[scoremat] = parseblast(infile)
	print(f'{scoremat}\t{all_data[scoremat]["percid"]}\t{all_data[scoremat]["alen"]}\t{all_data[scoremat]["evalue"]}')
