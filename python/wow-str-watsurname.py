#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#
# #%%
# def print_full_name(first_name, last_name):
#     return "Hello"+""+ first_name +""+last_name+ "!"+"You just delved into python."
# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)
#%%

def print_full_name(first_name, last_name):

   return f"Hello {first_name} {last_name}! You just delved into python."
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

#%%

def print_full_name(first_name, last_name):
    f="Hello" +" "+ first_name+" "+last_name+"!" +" "+ "You just delved into python."

    print(f)

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

#ahahahhahaha 

#%%
def print_full_name(first, last):
    s="Hello {} {}! You just delved into python."

    print(s.format(first,last)) #print s.format kullandi wow

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)