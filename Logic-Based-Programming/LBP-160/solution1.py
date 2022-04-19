# Solution:

def shareOneDigit(L):
    count = 0
    for i in range(n-1):
        for j in str(L[i]):
            if j in str(L[i+1]):
                count += 1
                break
    return count == n-1

n = int(input())
print(str(shareOneDigit([int(i) for i in input().split()])).lower())
