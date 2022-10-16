#!/usr/bin/env python3

class dna_sequence(object):
	def __init__(self, sequence, gene_name, organism):
		self.sequence = sequence
		self.gene_name = gene_name
		self.organism = organism
	
	def length(self):
		seqlen = len(self.sequence)
		return seqlen
	
	def nt_comp(self):
		nt_dict = {}
		nt_dict['A'] = self.sequence.count('A')
		nt_dict['T'] = self.sequence.count('T')
		nt_dict['C'] = self.sequence.count('C')
		nt_dict['G'] = self.sequence.count('G')
		return nt_dict
	
	def gc_content(self):
		gc_cont = (self.sequence.count('G') + self.sequence.count('C')) / len(self.sequence)
		return gc_cont

	def to_fasta(self):
		fa_str = f'>{self.gene_name}\n{self.sequence}'
		return fa_str

	def compare(self,dna_seq2):
		name_comp = self.gene_name == dna_seq2.gene_name
		seq_comp = self.sequence == dna_seq2.sequence
		org_comp = self.organism == dna_seq2.organism
		comp = name_comp and seq_comp and org_comp
		return comp

humangene = dna_sequence('ATGCGTAGGTCTAGCTTCGATCAATCGATCGGATCTTCGATCGATCTTCATA', 'gene1', 'human')
humangene2 = dna_sequence('ATGCGTAGGTCTAGCTTCGATCAATCGATCGGATCTTCGATCGATCTTCAT', 'gene1', 'human')
print(f'gene sequence: {humangene.sequence}')
print(f'gene name: {humangene.gene_name}')
print(f'organism: {humangene.organism}')
print(f'sequence length: {humangene.length()}')
print(f'nucleotide composition: {humangene.nt_comp()}')
print(f'GC content: {humangene.gc_content()}')
print(f'fasta format:\n{humangene.to_fasta()}')
print(f'genes 1 and 2 same? {humangene.compare(humangene2)}')
