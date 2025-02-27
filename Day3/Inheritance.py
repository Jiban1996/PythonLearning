#single type
class A:
    i="Class A variable of single type inheritance"
    def m1(self):
        print("class a method")
class B(A):
    j=A.i+"class B type"
    def m2(self):
        print("class b method")
        print(self.i)

b=B()
b.m1()
b.m2()
print(b.i)
print(b.j)
print("_--------___________________")

#Multilevel
print("_--------___________________")
class A:
    i=25
    def m1(self):
        print("class a method in multilevel")
class B(A):
    j=A.i
    def m2(self):
        print("class b method")
class C(B):
    def m2(self):
        print("class c method m3")

c=C()
c.m1()
c.m2()
#c.m3()
print(c.i)
print(c.j)
print("_--------___________________")



#Hierchcy Level Inheritance
print("_--------___________________")
class A:
    i=25
    def m1(self):
        print("class a method")
class B(A):
    j=A.i
    def m2(self):
        print("class b method")
        print(super().m1(),"useing super method to call parent class method inside child")
class C(A):
    def m3(self):
        print("class c method m3")

c=C()
c.m1()
c.m3()
print(c.i)
print("_--------___________________")


#Multiple
print("_Multiple Inheritance___________________")
class A:
    i="class A"
    def m1(self):
        print("class a method m1")
class B:
    i="class B"
    def m1(self):
        print("class b method m1")
class C(B,A):
    def m3(self):
        print("class c method m3")
c=C()
c.m1()  #child class prefernce or overrrding of parent class
print(c.i) #overridding the variable
print("_--------___________________")