#!/bin/python3

# https://www.hackerrank.com/challenges/plus-minus/problem

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
  posit = 0
  negat = 0
  zero = 0
  total = len(arr)

  for i in arr:
    if i > 0:
      posit += 1
    elif i < 0:
      negat += 1
    else:
      zero += 1
  
  print("{0:.6f}".format(posit / total))
  print("{0:.6f}".format(negat / total))
  print("{0:.6f}".format(zero / total))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
