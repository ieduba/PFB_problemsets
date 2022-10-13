#!/usr/bin/env python3
import sys
fav_key = sys.argv[1]
fav_thing = sys.argv[2]

favs = {'book' : 'cloud atlas', 'song' : 'that\'s alright', 'tree' : 'burr oak'}
#print(favs['book'])
#to_print = 'book'
#print(favs[to_print])
#print(favs['tree'])
#favs['organism'] = 'cat'
#to_print = 'organism'
#print(favs[to_print])
#favs['organism'] = 'dog'

favs[fav_key] = fav_thing

for key in favs:
	print(f'favorite {key}: {favs[key]}')
