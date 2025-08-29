# WORDS STARTING WITH 'A'

WordList=["apple","ace","banana","carrot"]

extract=lambda x: x[0]=="a"
result=filter(extract,WordList)

print(list(result))