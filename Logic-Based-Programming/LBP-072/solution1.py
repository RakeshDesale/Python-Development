# Solution:

def HelloBye(name,num):
    if num==1:
        return ("Hello "+name)
    else:
        return ("Bye "+name)

name=input()
print(HelloBye(name,int(input())))
