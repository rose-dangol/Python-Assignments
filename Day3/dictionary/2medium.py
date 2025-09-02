# 1. Check if the key "salary" exists in {"name": "Sam", "salary": 5000} 
people={
    "name": "Sam", 
    "salary": 5000
}
keys=people.keys()

if "salary" in keys:
    print("Present")

# 2. Merge two dictionaries {1: "a", 2: "b"} and {3: "c", 4: "d"} into one.
d1={1: "a", 2: "b"}
d2={3: "c", 4: "d"} 
d1.update(d2)
print(d1)

#3. Get all keys and all values separately from a dictionary.
print(d1.keys())
print(d1.values())

# Create a dictionary from two lists:   keys = ["a", "b", "c"] and values = [1, 2, 3]
keys = ["a", "b", "c"]
values = [1, 2, 3]

for i in range(len(keys)):
    dictList={
        keys[i]:values[i]
    }
# dictList=dict(zip(keys,values))
print(dictList)

# 5. Count how many times each letter appears in "banana" using a dictionary.
a="banana"
b={}
for x in a:
    if x in b:
        b[x]+=1
    else:
        b[x]=1

print(b)