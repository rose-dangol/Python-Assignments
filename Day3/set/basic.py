# unique and mutable elements no order

# 1. Create a set with the values {1, 2, 3, 4, 5} and print it.
s1={1, 2, 3, 4, 5}
print(s1)

# 2. Create an empty set and verify its type.
s2={}
print(type(s1))

# 3. Add an element "python" to a set.
s3={"java"}
s3.add("python")
print(s3)

# 4. Remove an element from a set using both .remove() and .discard() and observe
s4={"python","java","php","c"}
s4.remove("c")
print(s4)

s4.discard("c#")    #keyError didaina
print(s4)

# 5. Check if 10 exists in {5, 10, 15, 20} .
s5={5, 10, 15, 20}
if 10 in s5:
    print("yes")