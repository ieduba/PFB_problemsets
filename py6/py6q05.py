#!/usr/bin/env python3

with open('Python_06.txt','r') as rfile, open('Python_06_uc.txt','w') as wfile:
	for line in rfile:
		line = line.rstrip()
		line = line.upper()
	#	print(line)
		wfile.write(f'{line}\n')

