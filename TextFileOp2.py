#real the files and tsore into list
#reverse the list
#write the list back into file
from io import open

with open(r"C:\Users\KIIT\Desktop\PythonSelenium\Learing Python\Fils\Text2File.txt") as fileName:
    beforeData=fileName.readlines()
    for data in beforeData:
        print(data)
    beforeData.reverse()     #or you can use reversed(beforeData)
    #reversed(beforeData)
print("*********************************************")
with open(r"C:\Users\KIIT\Desktop\PythonSelenium\Learing Python\Fils\Text2File.txt","w") as writingData:
    for data in beforeData:
        writingData.write(data)

print("*********************************************")
with open(r"C:\Users\KIIT\Desktop\PythonSelenium\Learing Python\Fils\Text2File.txt","r") as fileName:
    ResultData=fileName.readlines()
    for data in ResultData:
        print(data)
