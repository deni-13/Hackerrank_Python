# https://www.hackerrank.com/challenges/find-a-string/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#%%
st1="ABCDCDC"
st2="CDC"
ortak=[]
for i in range(len(st1)):
    print(st1[i])
    print("-----------")
    for j in range(len(st2)):
        print(st2[j])
        if st2[j] == st1[i]:
            ortak.append(st2[j])
ortak=set(ortak)
ortak
o=len(ortak)
o

#print(ortak)

#%%

def count_substring(string, sub_string):
    ortak=[]
    for i in range(len(string)):
        #print(string[i])
        #print("-----------")
        for j in range(len(sub_string)):
            #print(sub_string[j])
            if sub_string[j] == string[i]:
                ortak.append(sub_string[j])

    ortak=set(ortak)
    o=len(ortak)
    return o
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


#%% alternatif:::

def count_substring(string, sub_string):
    count = 0
    substring_length = len(sub_string)  #substring boyu
    
    for i in range(len(string) - substring_length + 1):  #farklari kadar bakicam cunku birbirini iceriyoe
        if string[i:i + substring_length] == sub_string:
            count += 1
    
    return count