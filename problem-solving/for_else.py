#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gtTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    counter=0
    for k in range(max(a), min(b)+1): #katlari aldim
        for ae in a:
            if k%ae!=0:
                break
        else:
            for be in b:
                if be%k!=0:
                    break
            else:
                counter+=1
    return counter
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
