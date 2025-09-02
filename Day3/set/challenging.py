# 1. Given two sets, check if one is a subset of the other.
s1={1,2,3,4,5,6}
s11={2,4,6}

print(s11.issubset(s1))

# 2. Write a program to find elements that are in either of two sets but not in both.
s2={1,2,3}
s22={3,4,5}
print(s2.symmetric_difference(s22))

# 3. Use set comprehension to create a set of squares from 1 to 10.

# 4. Given a sentence, find all unique words using a set.
string="hello world"
s4=set(string)
s4.discard(" ")
print(s4)

# 5. Write a program that checks if two strings are anagrams using sets.
s5="race"
s55="care"
count=0
for x in s5:
    for y in s55:
        if x==y:
            count=count+1
            
if count==len(s5):
    print("yes anagram")
else:
    print("not anagram")