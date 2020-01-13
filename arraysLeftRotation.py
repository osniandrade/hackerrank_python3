#!/bin/python3

# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    while d > 0:
        a.append(a[0])
        del a[0]
        d -= 1
    
    #print(a)
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
