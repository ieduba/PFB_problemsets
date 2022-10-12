#!/usr/bin/env python3
import sys
import random

seq_str = sys.argv[1]
seq = list(seq_str)

for n in range(1,len(seq)):
	pos1 = random.randrange(n)
	pos2 = random.randrange(n)
	temp = seq[pos1]
	seq[pos1] = seq[pos2]
	seq[pos2] = temp
new_str = ''.join(seq)
print(new_str)
