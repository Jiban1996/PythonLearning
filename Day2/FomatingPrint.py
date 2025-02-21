Name="Jiban"
Age=29
Hight="5'7\""

#To Print

#Approach 1
print(Name)
print(Age)
print(Hight)


#Approach 2
print("my name is :",Name)
print("age is :",Age)
print("height is: ",Hight)


#Approach 3
print("my name is:%s Age is:%d height is:%s" %(Name,Age,Hight))

#  %s stand for STring
#  %d stand for Number
#  %g stand for decimal number

print("my name is:{} Age is:{} height is:{}".format(Name,Age,Hight))

num1=int(input("dd"))
num2=float(input("dd"))
print(num1+num2) #24.2