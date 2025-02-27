myDic={"Employye no1":24,"Empl2 ":45,"empl3 ":"jiban"}
print(myDic)
print(myDic["Empl2 "])
print(myDic.get("Employye no1"))
for i in myDic:
    str=myDic[i]
    if str==45:
        print("yes")
        break