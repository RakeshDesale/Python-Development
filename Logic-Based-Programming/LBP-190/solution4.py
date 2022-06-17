# Using Function

# Solution:

def isJackpot(L):
    L.sort()
    flag = True
    for i in range(len(L)-1):
        if(abs(L[i] - L[i+1]) > 2):
            flag = False
            break
    return flag

print("Yes" if isJackpot([int(i) for i in input()]) else "No")
