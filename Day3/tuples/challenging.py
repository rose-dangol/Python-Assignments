# 1. Write a program to remove an element from a tuple (without directly modifying it).
tt=(1,2,3,4,5)
listT1=list(tt)

listT1.remove(3)
print(tuple(listT1))

# 2. Given t = (("a", 1), ("b", 2), ("c", 3)) , convert it into a dictionary.
t = (("a", 1), ("b", 2), ("c", 3))
a={}
for i, j in t:
   a[i]=j
print(type(a)) 

# 3. Swap two tuples:
# t1 = (1, 2) and t2 = (3, 4) → after swap t1 = (3, 4) , t2 = (1, 2) .
t1 = (1, 2)
t2 = (3, 4)
        # t1,t2=t2,t1
temp=t1
t1=t2
t2=temp
print(f"T1:{t1}")
print(f"T2:{t2}")

# 4. Reverse a tuple without using slicing.
t4=(2,4,6,8)
listT4=list(t4)
left=0
right=len(t4)-1
while(left<right):
    listT4[left],listT4[right]=listT4[right],listT4[left]
    left=left+1
    right=right-1

print(tuple(listT4))

# 5. Create a tuple from user input where values are comma-separated.
input = input("Enter tuple elements:")
t5=tuple(input)
        # print(t5) yo garda it takes commas too so we gotta print every other element(ALTERNATE)
print(t5[0:len(t5):2])

