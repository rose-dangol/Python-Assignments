# lambda function
    # lambda arguments:expression
'''
# def func(number):
#     print(number*number)    #number**2 vaneko square
# func(3)

def square(num):
    return num **2

result= square(4)
print(result)

#square of two number using lambda function
square= lambda num:num**2 
print(square(6))

#sum of two number using lambda function
def sum(a,b):
    return a+b
res=sum(2,3)
print(res)


addition=lambda a,b:a+b
print(addition(3,4))

#CONDITIONAL
def check(number):
    if(number%2==0):
        print("even")
    else:
        print("odd")
check(4)

check = lambda num: 'Even' if num%2==0 else 'Odd'
print(check(4))

#map function 
        #map(function,iterables)
        # python sas a first class citizen??
a=[1,2,3,4,5]
def square(num):
    return num**2
result= map(square,a)
print(set(result))  #result is actually object so list() le object->list banaucha


#map function with lambda
numbers =[1,2,3,4]
sq= lambda num:num**2

res= map(sq,numbers)
print(list(res))


a=[1,2,3,4,5,6]
def check(num):
    if(num%2==0):
        return num
    
result= filter(check,a)
print(list(result))

a=[1,2,3,4,5,6]

# function = lambda num: True if num%2==0 else False
function= lambda num: num%2==0

result = filter(function,a)
print(list(result))
'''

from functools import reduce

num=[1,2,3,4,5,6]
def add(a,b):
    return a+b
result= reduce(add,num)
print(result)

#lambda function
num=[1,2,3,4,5,6]
add = lambda a,b:a+b
result = reduce(add,num)
print(result)

