# product of all numbers in a given list
from functools import reduce

number=[1,2,3,4,5]

product = lambda a,b:a*b
res = reduce(product,number)
print(f"Product of all numbers: {res}")