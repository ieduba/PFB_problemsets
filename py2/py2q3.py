#!/usr/bin/env python3
import sys

num = sys.argv[1]

num = int(num)
print('num:',num)

if num > 0:
	if num < 50:
		if num%2 == 0:
			print('even number smaller than 50')
		else:
			print('odd number smaller than 50')
	elif num > 50:
		if num%3 == 0:
			print('larger than 50, divisible by 3')
		else:
			print('larger than 50, not divisible by 3')
	else:
		print('fifty!')
elif num < 0:
	print('negative')
else:
	print('zero')
