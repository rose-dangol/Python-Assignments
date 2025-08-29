# #Mini Challenges

# print("Enter a string:")
# string = input()

# print(string[::-1])  #reverse

# #palindrome
# reversedString =string[::-1] 
# if string == reversedString:
#     print("Given string is a palindrome.")

# #count number of words
# spaceCount=0
# print("Enter a sentence:")
# userInput = input()
# for x in userInput:
#     if x==" ":
#         spaceCount=spaceCount+1 

# words= spaceCount+1
# print(f"Number of words: {words}")


#replace vowel with *
userInput = input("enter your word:")

vowels="aeiou"

for i in vowels:
    userInput=userInput.replace(i,"*")

print(userInput)

