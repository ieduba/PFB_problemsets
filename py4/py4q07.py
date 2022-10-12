#!/usr/bin/env python3

nums = [101,2,15,22,95,33,2,27,72,15,52]
st_nums = sorted(nums)

evensum = 0
oddsum = 0
for num in st_nums:
	print(num)
	if num%2 == 0:
		evensum = evensum + num
	else:
		oddsum = oddsum + num

print(f'sum of even numbers: {evensum}')
print(f'sum of odd numbers: {oddsum}')
	
