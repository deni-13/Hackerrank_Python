# https://www.hackerrank.com/challenges/string-validators/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
#%%
# s="qA2"


s = "#$%@^&*kjnk svskjnbui h 4oi3hheuh /dfh uidshvhdsuihv suihc 0hrem89m4c02mw4xo;,wh fwhncoishmxlxfkjsahnxu83v 08 n8OHOIHIOMOICWHOFCMHEOFMCOEJMC0J09C 03J J3L;JMFC3JM3JC3'JIOO9MMJ099U N090N9 OOHOLNHNLLKNLKNKNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333000000000000000000000000000000000000000000000000000000000000000000000000000"


# s = ''.join(e for e in s if e not in ls)
# print(s)
s=s.replace(" ","")
l=set(s)
a=""
for i in l:
    a+=i
print(a)
s=a
s
print(s[::].isalnum())
print(s[0:1].isalpha())
print(s[2].isdigit())
print(s[0].islower())
print(s[1].isupper())



# s="#$%@^&*k"

# s.isalnum()

#%%
if __name__ == '__main__':
    s = input()
    print(
        any(map(str.isalnum,s)),
        any(map(str.isalpha,s)),
        any(map(str.isdigit,s)),
        any(map(str.islower,s)),
        any(map(str.isupper,s)),
        sep = "\n"
    )

#any fonk kullanimi:
#%%

# ny() fonksiyonu, all() fonksiyonunun tersidir.

# any() fonksiyonunda,
# dizisel verilen tipin içerisindeki elemanların 
# hepsi _True_ise True döndürürken bir tanesi False olsa False döndürüyordu.

#any nin kendisi 


def a(lst):
    if "a" in lst:
        return True

    return False

lst1=[True,False,True,False]

any(lst1)