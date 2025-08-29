#length of each string

StringList=["abc","defgh","helloo"]
lengthCheck = lambda list:len(list)

res= map(lengthCheck,StringList)
print((list(res)))