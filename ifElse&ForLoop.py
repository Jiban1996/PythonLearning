# if else

Greeting ="Good Morning "
if Greeting == "Good Morning ":  # comparing always case-sensitive and space sensitive
    print("Condition matches")
else:
    print("Not matching")
print("not part of ifElse")

Number = 45
if Number < 45.5:  # comparing always case-sensitive and space sensitive
    print("Condition matches")
else:
    print("Not matching")
print("not part of ifElse")

age = 35
salary = 6000

# add two conditions using and operator
if age >= 30 and salary >= 5000:
    print('Eligible for the premium membership.')
else:
    print('Not eligible for the premium membership')