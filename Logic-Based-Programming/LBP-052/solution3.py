# Another Approach Using Function

# Solution:

def stoneCount(jw,st):
    counter=0
    for i in jw:
        counter=counter+st.count(i)
    return counter

jw=input()
st=input()
print(stoneCount(jw,st))
