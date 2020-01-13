#!/bin/python3

# https://www.hackerrank.com/challenges/compare-the-triplets/problem

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    bob = 0
    alice = 0
    cont = 0

    for i in a:
        if a[cont] > b[cont]:
            alice += 1
        elif a[cont] < b[cont]:
            bob += 1
        cont += 1
    
    return [alice, bob]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()