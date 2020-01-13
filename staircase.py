#!/bin/python3

# https://www.hackerrank.com/challenges/staircase/problem

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
  degraus = n - 1
  stairs = []

  while degraus >= 0:
    stairs.append(' ')
    degraus -= 1

  while degraus < n - 1:
    stairs.pop(0)
    stairs.append('#')
    linha = "".join(stairs)
    print(linha)
    degraus += 1

if __name__ == '__main__':
    n = int(input())

    staircase(n)
