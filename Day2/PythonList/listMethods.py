numbers = [5, 2, 9, 1, 5, 6]
fruits = ["apple", "banana", "cherry"]

#1. Append "orange" to fruits
fruits.append("orange")

# 2. Insert "kiwi" at index 1 in fruits .
fruits.insert(1,"kiwi")
print(fruits)

# 3. Remove "banana" from fruits .
fruits.remove("banana")
print(fruits)

# 4. Pop the last item from numbers .
numbers.pop(len(numbers)-1)
print(numbers)

# 5. Clear all elements from a copy of fruits .
fruitsCopy=list(fruits)
print(fruitsCopy)
fruitsCopy.clear()
print(fruitsCopy)

# 6. Sort numbers in ascending order.
numbers.sort()
print(numbers)

# 7. Sort numbers in descending order.
numbers.sort(reverse=True)
print(numbers)

# 8. Reverse fruits without sorting.
left=0
right=len(numbers)-1

while(left<right):
    temp= numbers[left]
    numbers[left]=numbers[right]
    numbers[right]=temp
    left = left+1
    right=right-1
print(numbers)

# 9. Sort fruits alphabetically.
fruits.sort()
print(fruits)

# 10. Count how many times 5 appears in numbers.
count=0
for x in numbers:
    if x ==5:
        count=count+1
print(count)

# 11. Find the index of "cherry" in fruits .
print(fruits)
length=len(fruits)
i =0
index=-1
while i<length:
    if fruits[i]=="cherry":
        index=i
    i=i+1

print(f"Index of cherry: {index}")

# 12. Create a shallow copy of numbers and modify it — check if the original changes.
numbersCopy = numbers.copy()
numbersCopy.append(23)

print(numbersCopy)
print(numbers)