#to check if a string is a palindrome

check = lambda string:string==string[::-1]
check("abcsba")
if(check=="True"):
    print("String is a palindrome")
else:
    print("String is not a palindrome")