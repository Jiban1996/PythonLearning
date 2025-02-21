print("hello")

# for commenting anything

a = 3
print(a)
# NO NEED TO declare any data type as like Java
a = "string"
print(a)
# NO NEED TO declare any data type as like Java

b, c, d = 5, 6.5, "strubf"
print(b)  # 5
print(type(b))  # <class 'int'>
print(type(c))
print(c)  # 6.5
print(d)   # strubf

# How to use string concatenation using format method
b = 15
print("{} {} {}".format("value is ", b ,"is correct"))
print("value is ", b)
# we can concanate two string like java as example given below
m = "String 2"
print("string1 is concanated with "+m)    # string1 is concanated with String 2
m = 4
print(4+m)  # 8


name , age, hight="jiban",29,"5'8\""
print(name)
print(age)
print(hight)

import  sys
print(sys.version)

# Python data Types
# Numeric
# String
# List
# Tuple
# Dictionary


fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

"""If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. T
he global variable with the same name will remain as it was, global and with the original value.
"""
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)