#!/bin/python3

# https://www.hackerrank.com/challenges/counting-valleys/problem

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level = 0
    valleys = 0
    in_valley = 0
    
    for step in s:
        if step == 'U':
            level += 1
        elif step == 'D':
            level -= 1
    
        if level < 0 and in_valley == 0:
            in_valley = 1
            valleys += 1
        elif level == 0 and in_valley == 1:
            in_valley = 0
    
    return(valleys)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
