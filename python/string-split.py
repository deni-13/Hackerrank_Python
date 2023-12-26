# https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

#%%
line="u are mine"

line=line.split(" ")

a= "-".join(line)
a
#%% sol

def split_and_join(line):
    line=line.split(" ")

    return "-".join(line)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)