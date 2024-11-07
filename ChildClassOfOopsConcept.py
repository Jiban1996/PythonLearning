from OopsConcepts import Calculator


class childClass(Calculator):
    print("nothing")
    def __init__(self):
        Calculator.__init__(self,5,15)
    def allData(self):
        return self.Summation()
obj1=childClass()
print(obj1.allData())



