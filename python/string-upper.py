# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2  
#%%
s="Www.HackerRank.com"
new=""
for i in s:
    if i==i.upper():
        new+=i.lower()
    else:
        new+=i.upper()
print(new)
