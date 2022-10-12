#!/usr/bin/env python3

i = 1
fac = 1
while i < 1001:
	fac = fac*i
	i+=1

fac_magnitude = len(str(fac))-1
fac_trunc = str(fac)[0:4]
fac_list = list(fac_trunc)
fac_list.insert(1,'.')
fac_dec = ''.join(fac_list)
print(f'{fac_dec}x10^{fac_magnitude}')

#print(fac)
