#Exceptions are errors that occur at runtime when the program is being executed.
# They are usually caused by invalid user input or code that is invalid in Python.
# Exception handling allows the program to continue to execute even if an error occurs.


#in here you can also give tes validation to give exception dynamically like
i=3
if i!=3:
    raise Exception("Validation check failed to so test Case raise exception")

#you can use assert for validation like

ii=2
assert (ii==22) #when compare fails it will failed the test case
