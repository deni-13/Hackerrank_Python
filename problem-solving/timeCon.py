# https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true




#%%
def timeConversion(s):

    if s[8]=="P":
        if s[:2]=="12":
            return s[:-2]
        else:
            return str(int(s[:2])+12)+s[2:-2]
    else:
        if s[:2]=="12":
            return "00"+ s[2:-2]
        else:
            return s[:-2]

#%%
s="12"
str(int(s)-6)

#%% date time cozum



import datetime
#24lik sistem
def Timc(S):
    tarih=datetime.datetime.strptime(S,"%I:%M:%S%p").time()
    print(str(tarih))


Timc("07:00:00PM")

#%%hr cozum
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
import datetime
def timeConversion(s):

    tarih=datetime.datetime.strptime(s,"%I:%M:%S%p")
    tarih_str=datetime.datetime.strftime(tarih,"%H:%M:%S")
    return (tarih_str)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
