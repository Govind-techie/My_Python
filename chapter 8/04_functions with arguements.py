# FUNCTIONS WITH ARGUMENTS
# A function can accept some value it can work with. We can put these values in the parentheses.


def b(a,b): # (a) and (b) are 2 arguments of given function
    print("Good day " + (a))
    print(b)
    return "done" # return gives a certain value to the variable containing function

c = b("Govind", "Thank You") # the value "Govind" and "Thank You" get assigned to 2 given arguments (a) and (b)
print(c)
