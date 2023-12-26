# def solve(s):
    

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     result = solve(s)

#     fptr.write(result + '\n')

#     fptr.close()
#%%

s="chris alan".split(" ")
s #bu bir liste

for i in s:
    print(i[0].upper()+i[1::],end=" ")
#%%

def solve(s):
    for i in s.split():
        s=s.replace(i,i.capitalize())
    return s
    



# https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true