#%%
import numpy

# Read n, m
n, _ = map(int, input().split())

# Read Array
array = [list(map(int, input().split())) for _ in range(n)]

# Opperations
print(numpy.transpose(array))
print(numpy.array(array).flatten())
# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem


#%%
# arr1=numpy.array([[3,2],[1,2],[3,4],[5,6]])
# arr1
# t=arr1[1:,::]
# t
# t.transpose()
