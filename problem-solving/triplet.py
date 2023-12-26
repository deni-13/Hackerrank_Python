# # https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true
#%%
l=[1,2,9]
n=[0,6,3]
puana=0
puan=0
for ind1,i in enumerate(l):
    for ind2,j in enumerate(n):
        if ind1==ind2:
            if i>j:
                puan+=1
            elif i==j:
                puan+=0
            else:
                puana+=1

[puan,puana]

#%%
import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    puana=0
    puan=0
    for ind1,i in enumerate(a):
        for ind2,j in enumerate(b):
            if ind1==ind2:
                if i>j:
                    puan+=1
                elif i==j:
                    puan+=0
                else:
                    puana+=1

    return [puan,puana]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
#%%  alternatif


def compareTriplets(a, b):
    alice,bob=0,0
    for i in range(3):
        if a[i]>b[i]:
            alice+=1
        elif a[i]<b[i]:
            bob+=1
    return [alice,bob]

l=[1,2,9]
n=[0,6,3]
res=compareTriplets(l,n)
print(res)


#%%
a=[1,2,9]
b=[0,6,3]

alice=sum(1 if a[i]>b[i] else 0 for i in range(3))
bob=sum(1 if a[i]<b[i] else 0 for i in range(3))

print( [alice,bob])