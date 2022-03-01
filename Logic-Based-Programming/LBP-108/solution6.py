# Traditional Approach Using Function

# Solution:

def arrsum(L):
    sum=0
    for i in L:
        if i%10==3:
            sum = sum+i
    return sum

n = int(input())
print(arrsum([int(i) for i in input().split()]))
