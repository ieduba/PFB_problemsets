#!/usr/bin/env python3
import sys

var = sys.argv[1]

falsethings = ('0', 'None', 'False', '[]', '()', '')

if var not in falsethings:
	print('value is true')
else:
	print('value is not true')
