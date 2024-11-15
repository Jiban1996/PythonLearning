# For Loop

listValue = [12, 15.65, "String Value"]
for i in listValue:     # no need to call size() like in java default it will iterate until list size
    print(i)
    print(listValue)

NumValue = [12, 15.65, 99, 105]
for i in NumValue:
    print(i*2)  # 24 31.3 198 210

NumValue2 = [12, 15.65, 99, 105]
for j in range(2):
    print(NumValue2[0])  # 12  12

for l in range (1, 6):    # it will iterate 1 to 5 ny defualt l++
 print(l)

for t in range (1, 10,2):    # it will iterate 1 to 9 and if you want increment 2
 print( t )

print("****** ************************")

# how many times the number 1 appears in the list num
num = [1 , 15 , 1]
count =0
for i in num:
    if i==1:
        count +=1
print(count)

print("****** ************************")
# how many times the number 1 appears in the list num
num = [1 , 15 , 1]
count =0
for i in range(len(num)): #len is used for size of list
    if num[i]==1:
        count +=1
print(count)

print("****** ************************")
num3 = [1 , 15 , 63, 63 , 63]
count3 =0
for i in num3:
    if i==63:
        count3 +=1
print(count3)
print("****** ************************")

numDec=5
for num in range (6):
    print(num , "sf")
    num -= 1

for num in range(5, -1, -1):  # Start at 5, stop at -1, decrement by 1
    print(num)