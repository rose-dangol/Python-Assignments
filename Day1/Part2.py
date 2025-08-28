#String Conversion:

string = "learning python"

upperCase = string.upper()
lowerCase = string.lower()
titleCase= string.title()

print(upperCase)
print(lowerCase)
print(titleCase)

#Remove spaces

text =  " Clean Me "
text= text.replace(" ","")
print(text)

# Replace "dog" with "cat" in "I have a dog" .
replacetxt= "I have a dog"
replacetxt= replacetxt.replace("dog","cat")
print(replacetxt)

# 4. Count how many times "a" appears in "Banana" .
count=0
countText="Banana"
for x in countText:
    if (x=="a"):
        count=count+1;
print(count)