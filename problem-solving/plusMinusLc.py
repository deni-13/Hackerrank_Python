
#%%
arr=[1,-1,3,5,-1,3]

payda=len(arr)


print(sum(1 for i in arr if i>0)/payda)
print(sum(1 for i in arr if i<0)/payda)
print(sum(1 for i in arr if i==0)/payda)


# print(len([i for i in arr if i>0])/payda)
# print(len([i for i in arr if i<0])/payda)
# print(len([i for i in arr if i==0])/payda)
