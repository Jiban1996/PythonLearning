fileData=open("Fils/TextFile.txt")
data=fileData.read() #to read all data
lines = fileData.readlines()  #returns all the lines in file in list
line_count = len(lines)
print(line_count)
print(data)
fileData.close()
print("*****************************")

fileData=open("Fils/TextFile.txt")
data1 = fileData.read(3)  #if you want first 3 charactor
print(data1)
fileData.close()
print("*****************************")


fileData=open("Fils/TextFile.txt")

data2 = fileData.readline() #if you want read 1st line wise
data3 = fileData.readline() #if you want read 2st line wise
print(data2)
print(data3)
fileData.close()

print("*****************************")
fileData=open(r"C:\Users\KIIT\Desktop\PythonSelenium\Learing Python\TextFile.txt " ) # opening the file and wrote "r" before path to take path as string
lines = fileData.readlines()  # readline is retusn singlle line and read lines returns all the line and  you can store in list
line_count = len(lines) # using lenth method to get no of lines presnt in that file
print(line_count)
fileData.close()

print("*****************************")
fileData=open("Fils/TextFile.txt")  #using while loop to print all the lines
lin2=fileData.readline()
while lin2!="":
    print(lin2)
    lin2 = fileData.readline()
print("*****************************")