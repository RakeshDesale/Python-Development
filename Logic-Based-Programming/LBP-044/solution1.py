# Solution:

def diff(l):
    sumeven=0
    sumodd=0
    for i in l:
        if i%2==0:
            sumeven+=i
        else:
            sumodd+=i
    return sumeven-sumodd

n=int(input())
l=[int (i) for i in input().split()]
print(abs(diff(l)))
