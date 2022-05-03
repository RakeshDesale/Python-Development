# Solution:

W1,W2,W3,L1,L2 = (int(i) for i in input().split())
print("Yes" if W1+W2+W3 <= L1+L2 else "No")
