# Without Using Function

# Solution:

n = int(input())
L = [i for i in input().split()]
flag = False
for i in L:
    if '7' in i:
        flag = True
        break
print("Boom!" if flag else "there is no 7 in the array")
