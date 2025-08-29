'''
1. Create a list of 5 favorite movies.
2. Create a list with mixed data types ( int , str , float , bool ).
3. Create a nested list (list inside another list).
4. Access the first element of a list.
5. Access the middle element of a list.
'''

movieList=["27 Dresses", "Little Woman","Ironman","Red","Baby"]

mixedList=["abc",123,23.56, True]

nestedList =[["one","two","three"],[1,2,3]]

firstElement=movieList[0]
print(firstElement)

middleIndex= len(movieList)//2
print(movieList[middleIndex])


'''
6. Access the last element of a list.
7. Use negative indexing to get the second-last element.
8. Print the first 3 elements of a list using slicing.
9. Print the last 3 elements of a list using slicing.
10. Reverse a list using slicing.
'''
lastIndex = len(movieList)-1
lastElement = movieList[lastIndex]
print(lastElement)

print(movieList[-2])

print(movieList[0:3])

print(movieList[-3:])

print(movieList[::-1])
'''
11. Replace the second element with "Python" .
12. Change the last two elements to "Done" and "Finish" .
13. Concatenate two lists.
14. Repeat a list 3 times using .
15. Check if "apple" exists in a list using the in operator.
'''

movieList[1]="Python"
print(movieList)

length=len(movieList)
movieList[length-2]="Done"
movieList[length-1]="Finish"
print(movieList)

newList=["new","data","to","add"]
concatenatedList=movieList+newList
print(concatenatedList)

print(newList*3)

res= "apple" in movieList
if res=="False":
    print("'apple' is not present in the list")
else:
    print(" 'apple' is present in the list")
