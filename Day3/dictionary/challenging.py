# # 1. Write a program to get the key with the maximum value in a dictionary.
dictionary = {
    "one":1,
    "two": 2,
    "three": 3
}
# print(dictionary.items())
max= 0
maxKey=None
for key, value in dictionary.items(): 
    if max<value:
        max=value
        maxKey=key
print(maxKey)

# # 2. Invert a dictionary so that its values become keys and keys become 
dictionaryA={
    "eng":"abc",
    "age":22,
    "place":"ktm"
}
dictionaryB={    }   
for keys,val in dictionaryA.items():
    dictionaryB[val]=keys

print(dictionaryB)


# # Given a nested dictionary of student details, print the engs of students who scored more than 80 in math.
students={
    "jess" : {
    "eng" : 24,
    "math" : 45
  },
      "emily" : {
    "eng" : 89,
    "math" : 80
  },
      "rory" : {
    "eng" : 32,
    "math" : 90
  },
      "richard" : {
    "eng" : 32,
    "math" : 92
  },
      "dean" : {
    "eng" : 23,
    "math" : 80
  }
}

# print(students.items())
for i, obj in students.items():
    # print(obj)
    for a,b in obj.items():
        # print(a)
        if(a=="math"):
            if(b>80):
                print(i)
   
# # 4. Write a program to sort a dictionary by its values in ascending order.
d4={
    "five":5,
    "one":1,
    "three": 3,
    "two": 2
}


# # 5. Remove all keys from a dictionary that have None as a value.
d5={
    "hi":21,
    "hello":13,
    "bye": None,
    "ok":None
}
keyss=[ ]
for k,v in d5.items():
    if (v==None):
        keyss.append(k)
        # del d5[k]     

for ks in keyss:
    del d5[ks]
print(d5)