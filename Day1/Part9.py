# # Username Generator
print("Enter first name:")
firstName= input()

print("Enter last name:")
lastName= input()

print("Enter birth year:")
birthYear=input()

print(f"{firstName}.{lastName}{birthYear}")

#Password Generator
print("Enter a word:")
word= input()

password = word[::-1].upper() + "3"
print(password)

#Pig Latin Converter
string = "python"

pigLatin=string + "ay"
print(pigLatin)