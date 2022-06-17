# Using Function and Using sorted Inbuilt Method

# Solution:

def isJackpot(L):
    L = sorted(L)
    flag = True
    for i in range(len(L)-1):
        if(abs(L[i] - L[i+1]) > 2):
            flag = False
            break
    return flag

print("Yes" if isJackpot([int(i) for i in input()]) else "No")
