import math
import os
import random
import re
import sys

def weirdos(n):
    if n%2==0 and 2<=n<5 or n>20:   #tek bir ifle not weirdi topladık
        return (" Not Weird") 
    return "Weird"

#not weird 

if __name__ == '__main__':
    n = int(input().strip())
    print(weirdos(n))
#tek satir
print(" Not Weird" if n%2==0 and 2<=n<5 or n>20 else "Weird" )