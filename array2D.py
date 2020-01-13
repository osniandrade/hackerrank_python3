#!/bin/python3

# https://www.hackerrank.com/challenges/2d-array/problem

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    pos_x = 0
    pos_y = 0
    hrglss = []
    
    
    x = len(arr[0])
    y = len(arr)
    
    if x > 3 and y > 3:
        while pos_x + 2 < x:
            while pos_y + 2 < y:
                soma = arr[pos_y][pos_x] + arr[pos_y][pos_x+1] + arr[pos_y][pos_x+2]
                soma += arr[pos_y+1][pos_x+1]
                soma += arr[pos_y+2][pos_x] + arr[pos_y+2][pos_x+1] + arr[pos_y+2][pos_x+2]
    
                hrglss.append(soma)
    
                soma = 0
                pos_y += 1
            pos_y = 0
            pos_x += 1
        pos_x = 0
    else:
        #print(None)
        return None
    
    highest = max(hrglss)
    
    #print(hrglss)
    #print(highest)
    return highest
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
