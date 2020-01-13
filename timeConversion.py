#!/bin/python3

import os
import sys

# https://www.hackerrank.com/challenges/time-conversion/problem

#
# Complete the timeConversion function below.
#
def timeConversion(s):
  swt = 0

  if s[0] == '0' and s[8] == 'A':
    swt = 1

  time = s.split(':')
  time[0] = int(time[0])

  if time[2][2] == 'P':
    if time[0] != 12:
      time[0] += 12
  elif time[2][2] == 'A':
    if time[0] == 12:
      time[0] = '00'

  time[0] = str(time[0])

  time = ":".join(time)
  time = time[:-2]

  if swt == 1:
    time = '0' + time

  return time

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
