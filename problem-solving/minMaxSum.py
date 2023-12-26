#%%
import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    t=sorted(arr)
    print(sum(t[0:-1]), +sum(t[1::]),sep=" ")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
#%%

arr=[1,3,5,7,9]

sorted(arr)

mi=sum(arr[0:-1])
mi

ma=sum(arr[1::])
ma



#%%
def miniMaxSum(arr):
    t=sorted(arr)
    #a= sum(t[0:-1])+  "" +sum(t[1::])
    print(sum(t[0:-1]), +sum(t[1::]),sep=" ")

miniMaxSum([1,2,3,4,5])

#%%
# sort ile sorted arası fark 

a=[1,2,3,5]

sorted(a)

#orjinalini degistirmez

a.sort() #bu orjisnalini degistirir

