# Solution:

def firstVowel(s):
    for i in range(len(s)):
        if s[i] in "aeiou":
            return i

print(firstVowel(input()))
