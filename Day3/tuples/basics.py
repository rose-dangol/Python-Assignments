# 1. Create a tuple containing five colors. Print the second and fourth color.
colors=("red","green","blue","yellow","pink")

print(colors[1])
print(colors[3])

# 2. Create a tuple with a single element. Verify its type is tuple .
name=("rose",)
print(type(name))

name=("rose")
print(type(name))

# 3. Convert the list ["apple", "banana", "cherry"] into a tuple.
fruit=["apple", "banana", "cherry"] 
print(tuple(fruit))

# (1, 2, 3) and (4, 5, 6)
t1=(1, 2, 3)
t2=(4, 5, 6)
concatenate = t1+t2
print(concatenate)

# 5. Check whether "python" exists in the tuple ("java", "python", "c++") .
lang=("java", "python", "c++")
if "python" in lang:
    print("Present")
    
