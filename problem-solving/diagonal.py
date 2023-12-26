# https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

#test against custom inpu --- nested list


# [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
# diagonal1=arr[0][0]+arr[1][1]+arr[2][2]
# diogonal2=arr[len(arr)-1]

#%%
arr=[[11, 2, 4], [4, 5, 6], [10, 8, -12]]

s=len(arr)
kos1,kos2=0,0
for i in range(s):
    kos1+=arr[i][i]
for j in range(s):
    kos2+=arr[j][s-1-j]

print(kos1)
print(kos2)

abs(kos1-kos2)

#%%alt

uz=len(arr)
abs(sum( arr[i][i] for i in range(uz))-sum( arr[i][uz-1-i] for i in range(uz)))


