class Name:
    name="Jiban"
    age=30
    def __init__(self):
        print("f")
    def getData(self):
        print("i am just printing")

obj= Name()   #to create  Object in python just write like that no need to use new key word like java
print(obj.name)
print(obj.age)

obj.getData()