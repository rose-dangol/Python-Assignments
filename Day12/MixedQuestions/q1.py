#filter+map to fund square of even numbers

NumberList=[1,2,3,4,5,6,7,8,9]

evenExtract = filter(lambda num:num%2==0, NumberList)

# print(list(evenExtract))

result= map(lambda num:num**2, evenExtract)
print(list(result))
