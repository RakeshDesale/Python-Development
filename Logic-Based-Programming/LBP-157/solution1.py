# Solution:

def digit7Present(L):
    flag = False
    for i in L:
        if '7' in i:
            flag = True
            break
    return flag


n = int(input())
L = [i for i in input().split()]
print("Boom!" if digit7Present(L) else "there is no 7 in the array")
