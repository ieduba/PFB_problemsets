#!/usr/bin/env python3

setA = {3,14,15,9,26,5,35,9}
setB = {60,22,14,0,9}

ixn = setA & setB
diff = setA - setB
union = setA | setB
symdiff = setA ^ setB

print(f'''intersection: {ixn}
difference: {diff}
union: {union}
symmetrical difference: {symdiff}''')
