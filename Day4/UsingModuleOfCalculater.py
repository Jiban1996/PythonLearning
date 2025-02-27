#aPRROCH 1
import CalculaterModule
print(CalculaterModule.add(89,49))
print(CalculaterModule.sub(89,49))
print(CalculaterModule.multi(89,49))
print(CalculaterModule.div(89,49))
print(CalculaterModule.quat(89,49))
print(CalculaterModule.remain(89,49))

#aPRROCH 2
from CalculaterModule import add,multi
print(add(12,45))
print(multi(78,0))

#APRROCH 3 using * so i can access all the methods from that module
from CalculaterModule import *
print(add(12,45))
print(multi(78,0))

