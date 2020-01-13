#!/bin/python3

# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    way = len(c)
    cont = 0
    jump = 0

    while cont < way:
        if cont + 2 < way:
            if c[cont + 2] == 0:
                cont += 2
                jump += 1
            else:
                c[cont + 1] == 0
                cont += 1
                jump += 1
        elif c[cont + 1] == 0:
            cont += 1
            jump += 1
        if cont == way - 1:
            break
    
    return jump

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
