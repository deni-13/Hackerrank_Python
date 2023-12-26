#%%

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
#bas 1kucuk 

    if v1<=v2:
        print("NO")
    else:
        while x1<x2:
            x1+=v1
            x2+=v2
            if x1==x2:
                return("YES")
            
        return ("NO")
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()



#%%%

bas1=int(input())
v1=int(input())

bas2=int(input())
v2=int(input())


#bas 1kucuk 

if v1<=v2:
    print("no")
else:
    while bas1<bas2:
        bas1+=v1
        bas2+=v2
        if bas1==bas2:
            print("yes")
        else:
            print("no")


#%% hiz problemi gibi
x1=int(input())
v1=int(input())

x2=int(input())
v2=int(input())

mesafe=x1-x2
if v1>v2 and mesafe%v1-v2==0:
    print("yes")
else:
    print("no")