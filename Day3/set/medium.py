# 1. Find the union of {1, 2, 3} and {3, 4, 5} .
s1={1, 2, 3}
s11={3, 4, 5}

union=s1.union(s11)
print(union)

# 2. Find the intersection of {10, 20, 30} and {20, 40, 60} .
s2={10, 20, 30}
s22={20,40,60}
intersect=s2.intersection(s22)

print(intersect)

# 3. Find the difference between {1, 2, 3, 4} and {3, 4, 5, 6} .
s3={1, 2, 3, 4}
s33={3, 4, 5, 6}

diff=s3.difference(s33)
print(diff)

# 4. Create a set from a string and print it.
string="hello"
s4=set(string)
print(s4)

# 5. Remove duplicates from a list using a set.
l1=[1,2,3,1,2]
s5=set(l1)
print(s5)
