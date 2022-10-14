#!/usr/bin/env python3
import re

with open('Python_07_nobody.txt','r') as file, open('Python_07_Sylvia.txt','w') as newfile:
	poem = file.read()
	for nobody in re.finditer('Nobody',poem):
		print(f'position:{nobody.start()}')
	newpoem = re.sub('Nobody', 'Sylvia', poem)
	newfile.write(newpoem)
