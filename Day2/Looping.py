for i in range(1,11):
    print(i)
print("***********************")
for i in range(11):
    print(i)
print("***********************")
z=1
while z<11:
    print(z)
    z+=1

print("***********************")
x=10
while x>=1:
    print(x)
    x=x-1
print("***********************")
for k in range(10,0,-1):
    print(k)
print("Done !!")

for k in range(10,0,-1):
    if k==4 or k==6:
        continue
    print(k)
print("Done !!")
for k in range(1,10):
    if k==5:
        break
    print(k)
