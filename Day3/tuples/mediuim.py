# 1. Given nums = (10, 20, 30, 40) , unpack them into four variables and print each.
nums = (10, 20, 30, 40)
(var1,var2,var3,var4)= nums
print(var1)
print(var3)

# 2. Find the index of the first occurrence of 5 in (1, 5, 7, 5, 9) .
n=(1, 5, 7, 5, 9)
for x in range(len(n)):
    if n[x]==5:
        print(f"Index: {x}")
        break

# 3. Given t = ("a", "b", "c", "d", "e") , slice the tuple to get ("b", "c", "d") .
t = ("a", "b", "c", "d", "e")
t1=t[1:4]
print(t1)

# 4. Count how many times 2 appears in (2, 4, 2, 6, 2, 8) .
a=(2, 4, 2, 6, 2, 8)
count=0
for x in a:
    if x==2:
        count=count+1
print(count)

# 5. Merge two tuples and sort them into a new tuple.

a1=(2, 4, 6, 8)
a2=(3,5,7,9)
a12=sorted(a1+a2)  #yesai matra garda yo list huni raicha so tuple(a12)
print(tuple(a12))