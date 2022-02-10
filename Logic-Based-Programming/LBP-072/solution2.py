# Using Tuple

# Solution:

def HelloBye(name,num):
    if num==1:
        return ("Hello",name)
    else:
        return ("Bye",name)

name=input()
t=(HelloBye(name,int(input())))
for i in t:
    print(i,end=' ')
