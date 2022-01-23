# Using Inbuilt Functions

# Solution:

n1=[int (i) for i in input()]
n2=[int (i) for i in input()]
n3=[int (i) for i in input()]
w=min(n1[2],n2[2],n3[2])
x=min(n1[1],n2[1],n3[1])
y=min(n1[0],n2[0],n3[0])
z=max(max(n1),max(n2),max(n3))
print(z*1000+y*100+x*10+w)
