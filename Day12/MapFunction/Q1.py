#convert celcius to fahrenheit

temp = [31,45,38]
convert = lambda t:((t* 9/5) + 32)

fahrenheit = map(convert,temp)
print(list(fahrenheit))