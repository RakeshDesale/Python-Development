# Solution:

print("even" if bin(int(input()))[2::].count("1")%2==0 else "odd")
