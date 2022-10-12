#!/usr/bin/env python3
import sys

dna = sys.argv[1]

cdna0 = dna.replace('a','1').replace('t','2').replace('c','3').replace('g','4')
cdna1 = cdna0.lower()
cdna2 = cdna1.replace('a','T').replace('t','A').replace('c','G').replace('g','C')
cdna3 = cdna2.replace('1','t').replace('2','a').replace('3','g').replace('4','c')

rcdna = cdna3[::-1]

print(f'''Original Sequence\t5'{dna} 3'
Complement\t\t5'{cdna3} 3'
Reverse Complement\t5'{rcdna} 3'
''')
