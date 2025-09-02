# 1. Store your age in a variable and print it.
# 2. Store the price of an item (float) and print it.
# 3. Add, subtract, multiply, and divide two integers.
# 4. Divide two integers and show:
# Normal division ( / )
# Floor division ( // )
# Modulus ( % )
# 5. Multiply a float by an integer and print the result.
# 6. Use type() to check the data type of each result.
import math
age = 21
print(age)

price= 300.5
print(price)

res=abs(32-1.3)
print(res)

print(round(3.14159,2))

number="25.5"
no=float(number)
print(type(no))

#Convert seconds into hours, minutes, and seconds format.
totalSeconds=3805
hours = totalSeconds // 3600
seconds = totalSeconds % 3600
minutes = seconds // 60
seconds = seconds % 60

print(f"{hours:02}:{minutes:02}:{seconds:02}")

x1=2
y1=9

x2=5
y2=6

distance=math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))
print(distance)

