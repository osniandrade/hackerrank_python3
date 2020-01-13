#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/diagonal-difference/problem

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
  diag1 = 0
  sumDiag1 = 0
  diag2 = 0
  sumDiag2 = 0
  tamLinha = len(arr[0])

  diag2 = tamLinha - 1

  for i in arr:
    sumDiag1 += arr[diag1][diag1]
    sumDiag2 += arr[diag1][diag2]
    print(arr[diag1][diag1])
    print(arr[diag1][diag2])
    diag1 += 1
    diag2 -= 1
    
  return abs(sumDiag1 - sumDiag2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
