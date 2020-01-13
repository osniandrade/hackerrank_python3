#!/bin/python3

# https://www.hackerrank.com/challenges/repeated-string/problem

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    word = s
    str_size = n
    letter = 'a'
    letter_num = 0
    cont = 0
    
    string = []
    
    string = list(word)
    word_size = len(string)
    
    print(f'word_size = {word_size}')
    
    # in case the string is a single letter 'a'
    if word == letter:
        return str_size
        #print(str_size)
    
    extra = str_size % word_size
    repeats = int(str_size / word_size)
    
    print(f'extra = {extra}')
    print(f'repeats = {repeats}')
    
    letter_num = string.count(letter) * repeats
    
    if extra > 0:
        for i in string:
            if i == letter:
                letter_num += 1
    
            cont += 1
    
            if cont == extra:
                break
    
    return letter_num

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
