# https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true



#%%

s=[1,2,3,3]

max(s)
print(s.count(max(s)))

#%%
def birthdayCakeCandles(candles):
    print(candles.count(max(candles)))
birthdayCakeCandles([1,2,3,4,5,5,5])

#%%

def birthdayCakeCandles(candles):
    uzun =candles [0]
    counter = 0
    for i in candles:
        if i>uzun:
            uzun=i
            counter=1
        elif i==uzun:
            counter+=1
    return counter
birthdayCakeCandles([2,3,1,5,5])


#%% hr sol

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    uzun =max(candles)
    res=candles.count(uzun)
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()