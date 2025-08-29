#EVEN NUMBER FILTERING

NumberList= [1,2,3,4,5,6,7,8,9,10]

evenCheck = lambda num:num%2==0
res= filter(evenCheck,NumberList)

print(list(res))