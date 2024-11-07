# Tuple and  list are same but only differenc is Tuple is imMutable (we cant change the data , and inside Round  bracket )
# where List is mutable (we can change the data  and inside Sqaure bracket)


tupleValue = ("String ", 1, 2.5)
# tupleValue[0] ="dfadaf"
# del tupleValue[0]
print(tupleValue)
print(type(tupleValue))    # <class 'tuple'>
print(tupleValue[2])  # 2.5


# Dictionary concepts
# It is same like hashmap in java inside curly bracket key: value pair

dictionaryValue = {1: "first word ", "age": 45, 3: " third word"}
print(dictionaryValue["age"])  # 45
print(dictionaryValue[1])   # First word

# Declare dictionary for dynamic entry

dictionaryData = {}
dictionaryData["First Name"] = "Jiban"
dictionaryData["age"] = 45
print(dictionaryData)
