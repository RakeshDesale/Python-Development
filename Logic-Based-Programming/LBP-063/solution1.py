# Solution:

def countVowel(str):
    count=0
    for i in str:
        if i in 'aeiou':
            count+=1
    return count

print(countVowel(input()))
