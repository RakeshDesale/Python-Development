# Using Function

# Solution:

def highSaving(ms1,me1,ms2,me2,ms3,me3):
    return max(ms1-me1,ms2-me2,ms3-me3)

ms1,me1,ms2,me2,ms3,me3 = (int(i) for i in input().split())
print(highSaving(ms1,me1,ms2,me2,ms3,me3))
