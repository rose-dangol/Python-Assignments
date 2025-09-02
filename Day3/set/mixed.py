# # Mixed Tuple & Set
# . Create a tuple of numbers, convert it to a set, and then back to a tuple.
t1=(1,2,3,4,5)
print(tuple(set(t1)))

# 2. Given a list with duplicates, convert it to a tuple with only unique values.
l2=[1,2,2,3,4,3]
t2=tuple(set(l2))

print(t2)

# 3. Given t = (1, 2, 3, 2, 4, 1) , find all unique elements and store them in a set.
t3 = (1, 2, 3, 2, 4, 1)
s3=set(t3)
print(s3)

# 4. Store 5 tuples (name, age) in a set and display all people older than 25.
s4={("rose",22),("abby",27),("gracie",28),("charlie",28),("sab",20)}
for i,j in s4:
    # print(i)
    if j>25:
      print(i)

# 5. Find common elements between two tuples using sets.
t5=("apple","ball","cat","dog","ear")
t55=("ant","bat","cat","dog","elephat")

commonElemnt=(set(t5).intersection(set(t55)))
print(commonElemnt)