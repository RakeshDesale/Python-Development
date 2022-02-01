# Using Function

# Solution:

def shuffledString(st,arr):
    ts=[0]*len(st)
    for i in range(0,len(st)):
        ts[arr[i]]=st[i]
    return (''.join(ts))

st=input()
arr=[int (i) for i in input().split()]
print(shuffledString(st,arr))
