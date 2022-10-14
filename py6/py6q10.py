#!/usr/bin/env python3

with open('alpaca_all_genes.tsv', 'r') as allfile, open('alpaca_stemcellproliferation_genes.tsv', 'r') as scfile, open('alpaca_pigmentation_genes.tsv', 'r') as pigfile:

	all_gene_ids = []
	for line in allfile:
		if line[0] == 'G':
			continue
		geneid,gene_vers,trans_vers = line.split()
		all_gene_ids.append(geneid)
	unique_all = set(all_gene_ids)

	sc_gene_ids = []
	for line in scfile:
		if line[0] == 'G':
			continue
		geneid,gene_vers,trans_vers = line.split()
		sc_gene_ids.append(geneid)
	unique_sc = set(sc_gene_ids)

	pig_gene_ids = []
	for line in pigfile:
		if line[0] == 'G':
			continue
		geneid,gene_vers,trans_vers = line.split()
		pig_gene_ids.append(geneid)
	unique_pig = set(pig_gene_ids)

print(f'genes that are not proliferation: {unique_all - unique_sc}\nboth proliferation and pigment genes: {unique_sc & unique_pig}')

