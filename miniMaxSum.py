#!/bin/python3

# https://www.hackerrank.com/challenges/mini-max-sum/problem

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    totalSum = 0
    highSum = 0

    for i in arr:
        totalSum += i
  
    lowSum = totalSum

    for i in arr:
        if (totalSum - i) > highSum:
            highSum = totalSum - i
        if (totalSum - i) < lowSum:
            lowSum = totalSum - i

    print(lowSum, highSum)  

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
