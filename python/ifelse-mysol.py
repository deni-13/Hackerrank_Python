#%%
import math
import os
import random
import re
import sys

def weirdos(n):
    if n%2==1:
        return("Weird")
    else:
        if 6<=n<=20:
            return ("Weird")
        else:
            return (" Not Weird")  #direk diger kosullar burda!



if __name__ == '__main__':
    n = int(input().strip())
    print(weirdos(n))


#%%
n=24
if n%2==1:
    print("weird")
else:
    if n>20:
        print("not weird")
    if n<20:
        print(" weird")
    elif n<5:
        print(" not weird")