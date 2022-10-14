#!/usr/bin/env python3
import re

with open('Python_07.fasta','r') as file:
	fasta = file.read()
	for header in re.finditer('>(\S+)\s*(.*)\n',fasta):
		print(f'id: {header.group(1)}\tdesc: {header.group(2)}')
