class demo:
    def data1(self):
        pass  #you can not leave blank any method , you hav et write something or pass it
    def data2(self,God):
        print("Omm Namah Sivay")
        print(God)

demo().data2("Om")   #Demo() is the object and calling data2() method
varName=demo() #varName is the variable holding the object
varName.data2("Sivay")  #Omm Namah Sivay
varName.data1()

print("-----------------------------------------")
class demo1:
    def data1(self):
        print("intance method")
    @staticmethod
    def data2(self,God):
        print("Static method using static annotation")
        print(God)

demo1.data2(6,"namay")
d=demo1()
d.data2(7,78)


print("-----------------------------------------")
k,l=10,15 #Global Vriabele accesed anywhere
class myclass:
    i,j=40,50   #class variable can access using self keyword
    def addd(self,x,y): #local variable
        print(x+y)
        print(self.i+self.j)
        #print(k+l)  #as this is gloval so can access anywhere
        print(globals()['k']+ globals()['l'])  # using global function to call global variable inside a class
ObjectOfMyclas=myclass()
ObjectOfMyclas.addd(5,5)

print("-----------------------------------------")
#constructer examples
class cons():
    def __init__(self):
        print("its contsructer")

print("-----------------------------------------")
class emp:
    def __init__(self,ename,esal):
        self.name=ename
        self.sal=esal
    def display(self):
        print(self.name)
        print(self.sal)
    def __str__(self):
        return self.name  #This is one type of constructer which return string Data only
md=emp("Jiban",100000)
md.display()
print(md)  #it will print the ename as str constr. returns the ename string data
# and stroed inside md as it invoked when i create object of the class