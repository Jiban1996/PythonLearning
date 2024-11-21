
# List is like array in java

# value is like array in java , but  in here we can store any value in list
valuevariableList = ["string ", 5, 5.6]  #  in here value represent variable (list )
print(type(valuevariableList))  # <class 'list'>
valuevariableSet = {"string ", 5, 5.6}
valuevariableSet.add("string1 ")
print(valuevariableSet)
print(type(valuevariableSet))  # <class 'set'>


valuevariableSet = {"string ", "string2 ", "string3 ","string3 "}
print(type(valuevariableSet))
print("00000000000000000000000")
print(valuevariableSet)# <class 'set'>
valuevariableList = ["string ", "string2 ", "string3 "]
print(type(valuevariableList))   # <class 'List'>

valuevariableList = [5, 8, 15]
print(type(valuevariableList))   # <class 'List'>

# For List Sqaure Bracet
#  For Set Curly bracket



ListValue =[15, 15666, 5555, 9.6, "String Value "]
print(ListValue[4])   # "String Value "
print(ListValue[-1])   # "String Value " , -1 refers to last index in python
print(ListValue[1:4])   #  15666,5555,9.6 if you want to print certion range values , in her 4 is exclude from the index
ListValue.insert(2,"My name is Jiban")
ListValue.append("End Value") # if you want to insert any value value in the list at the end
ListValue[2] = "My name is Mohanty "  # if you want to update the value
del ListValue[1]   # if you want to delete  the value
print(ListValue)


list = [15, 445, 13]
listCpoy = list
listcopy2= listCpoy.copy()
print(listcopy2)
print(listCpoy)
list.reverse()
list.sort()
L = list
print(L)