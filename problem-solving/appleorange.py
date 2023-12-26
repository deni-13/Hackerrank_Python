#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    elma=0
    portakal=0
    k1=[]
    k2=[]
    for i in apples:
        k1.append(a+i)
    for j in oranges:
        k2.append(b+j)
    #print(k1,k2)

    for k in k1:  #k1 dizisi elemanlari aslinda koordinat elma
        if s<= k <=t:
            elma+=1
    for j in k2:
        if s<= j <= t:
            portakal+=1
            
    print(elma,portakal,sep="\n")
    
    
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
#%%

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

elma=0
portakal=0
k1=[]
k2=[]
for i in apples:
    k1.append(a+i)
for j in oranges:
    k2.append(b+j)
print(k1,k2)


for k in range(s,t+1):
    if k in k1 or k2 :
        elma+=1
        portakal+=1
print(elma,portakal,sep="\n")


#%%

