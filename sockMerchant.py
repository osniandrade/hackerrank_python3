#!/bin/python3

# https://www.hackerrank.com/challenges/sock-merchant/problem

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = []
    final = 0
    
    for sock in ar:
        if sock not in pairs:
            pairs.append(sock)
    
    for i in pairs:
        socks = ar.count(i)
    
        if socks > 1:
            while socks > 1:
                final += 1
                socks -= 2
    
    return final


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
