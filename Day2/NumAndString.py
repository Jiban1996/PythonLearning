a,b,c=15.8,18,200
d=max(a,b,c)  #max() returns the max value from given numbers
print(d)

a,b,c=15.5,18,200
d=min(a,b,c)  #min() returns the minimum value from given numbers
print(d)

#STring is immuatable (cant change the value if  we change the vale and new memomry allocated to the variable
#ex

str="Jiban"
print(id(str))  #id() returns adress of memory
#1685890355440

str=str+"MOhanty"
print(id(str))
#1685890355440 as it not match with privious memory so it String is Immuatable



#" +" used for conatation and "* " used for how many times you want to print for ex below

str="Kumar"
print(str+"mohnaty")   # KumarMOhanty

str="Kumar"
str12="Kumar"
print(str12.isalnum())
print("****1")
print(str.islower())
print(str.isupper())

print("****")
print(str.isalpha())
print("****")
print(str*3) #KumarKumarKumar
print(str[9:10])

a=[15,765,25,10.5]
print(max(a))

digiyt="454555s"
print(digiyt.isdigit())
STringName="JIban mohanty"
print(STringName.isspace())