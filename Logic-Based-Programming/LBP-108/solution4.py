# Using Function

# Solution:

def arrsum(n):
    return sum([int(i) for i in n if int(i)%10==3])

n = int(input())
print(arrsum([i for i in input().split()]))
