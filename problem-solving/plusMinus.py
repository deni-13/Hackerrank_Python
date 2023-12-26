# https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true


#%%
arr=[1,-1,3,5,-1,3]
poz=0
neg=0
sif=0
s=len(arr)
for i in arr:
    if i>0:
        poz+=1
    elif i==0:
        sif+=1
    else:
        neg+=1
print(poz/s,neg/s,sif/s,sep="\n")
#%%

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    poz,neg,sif =0,0,0
    s=len(arr)
    for i in arr:
        if i>0:
            poz+=1
        elif i<0:
            neg+=1
        else:
            sif+=1

    # print(poz/s)
    # print(neg/s)
    # print(sif/s)
    print(poz/s,neg/s,sif/s,sep="\n")
    if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
