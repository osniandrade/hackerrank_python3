#!/bin/python3

# https://www.hackerrank.com/challenges/a-very-big-sum/problem

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    # ar = ar.split()
    bigsum = 0

    for i in ar:
        bigsum += i

    return bigsum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()