# Using Function

# Solution:

def stoneCount(jw,st):
    count=0
    for i in jw:
        for j in st:
            if i==j:
                count+=1
    return count

jw=input()
st=input()
print(stoneCount(jw,st))
