# Using Function

# Solution:

def distanceOfEmp(L,sd,ed):
    for i in L:
        if abs(i)>=sd and abs(i)<=ed:
            print(i,end=' ')

n = int(input())
sd,ed = (int(i) for i in input().split())
distanceOfEmp([int(i) for i in input().split()],sd,ed)
