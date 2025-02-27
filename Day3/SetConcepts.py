mySet = {"string ",5, 5.6,"APple"}
#set is unindexed and unordered , unique,mutable

#accesing value of Set
# print(mySet[2]) giving error

for i in mySet:
    if i=="string ":
        print(i)

print("Printing all value")
for i in mySet:
    print(i)
print("cheching a vaklue or not -------------")
print("string " in mySet)
mySet.add(5)
