words=["apple","bag","cat","dog","egg"]

filteredWords = filter(lambda x:len(x)<4,words)
# print(list(filteredWords))

result= map(lambda a:a.upper(),filteredWords)
print(list(result))