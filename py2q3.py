#!/usr/bin/env python3
import sys

num = sys.argv[1]

num = int(num)

if num > 0:
	print('positive')
elif num < 0:
	print('negative')
else:
	print('zero')
