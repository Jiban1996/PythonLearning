def fuct():
    return
print(fuct())   #None

def fuct1():
    i=1 #Local variables

print(fuct1())  #None
def suma(a,b):
    print(a+b)
print(suma(14,38))

#Variables
x=100  #global variables
def num():
    global x
    y=200
    x=900
    print(y)
    print(x)
num()
print(x)


def data(i,j):
    print(i,j)
data(j=50,i=233)