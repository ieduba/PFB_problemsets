#!/usr/bin/env python3
import math
import sys

def entropy(sequence):
    fA = sequence.count('A')/len(sequence)
    fT = sequence.count('T')/len(sequence)
    fC = sequence.count('C')/len(sequence)
    fG = sequence.count('G')/len(sequence)
    
    forsum = []
    for freq in [fA,fT,fC,fG]:
        if freq == 0:
            continue
        else:
            product = freq * (math.log2(freq))
            forsum.append(product)
    
    shanent = -sum(forsum)
    return shanent

def main():
    sequence = sys.argv[1]
    shanent = entropy(sequence)
    print(shanent)

if __name__ == '__main__':
    main()
