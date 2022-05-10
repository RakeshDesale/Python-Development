# Solution:

ms1,me1,ms2,me2,ms3,me3 = (int(i) for i in input().split())
print(max(ms1-me1,ms2-me2,ms3-me3))
