#%%

j=int(input())

if j<40:
    f=(40-j)
    if f<3:
        j+=f
        print(j)
    else:
        print(j)
else:
    for i in range(1,5):
        if j%5==i:
            if i>=3:
                print(j+i-1)
            else:
                print(j)
#%%


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    puanlar=[]
    for i in grades:
        if i<38:
            puanlar.append(i)
        elif i %5>2: #67 kalan <3 ... 5 e bolumunden 3
            puanlar.append((i//5)*5+5)
        else:
            puanlar.append(i)
    return puanlar
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

        


#%% alt
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    puanlar=[]
    for i in grades:
        if i<38 or i %5<3 :
            puanlar.append(i)
        else:
            puanlar.append((i//5)*5+5)
    return puanlar
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
