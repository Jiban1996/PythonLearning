# we can declare method/function  using "def"  as like below
# no need to start the method using small case like  java

def demomethod():
    print("Demo method")
# function call
demomethod()

# parametrized function , in here no need to declare the the String name like java just write variable name
def demomethod1(name):
    print("Demo method")
    print(name+" Name is printing")

# function call
demomethod1("Jiban")

def sumofTwo(a , b):
    print(a+b)
sumofTwo(5,6)

def sumofTwo2(a , b):
    return a+b
print(sumofTwo2(5, 6 ))


k =int(input())
o =int(input())
def summm():
    print(k+o)
summm()
