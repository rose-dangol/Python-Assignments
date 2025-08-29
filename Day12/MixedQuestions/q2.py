#FILTER + REDUCE
from functools import reduce
number=[12,-4,3,-6,5,-5]

positiveNum= filter(lambda num:num>0,number)
# print(list(positiveNum)) 

sum = reduce(lambda a,b:a+b, positiveNum)
print(sum)