
#%%
def p2(n):
    res=""
    for i in range(1,n+1):
        res+=str(i)
    return res        
        
if __name__ == '__main__':
    n = int(input())
    r=p2(n)
    print(r)  