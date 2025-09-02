people={
    "name":"Rose",
    "age": 21,
    "city":"Kathmandu"
}
print(people)  #prints dictionary

q2={
    "name": "John", 
    "age": 25, "city": "London"
}
print(q2["age"]) #prints a single key's value

people["country"]="UK"  #create+update 
print(people)  

people["country"]="Paris"
print(people)

people.pop("age") #remove key
print(people.get("country1")) 
