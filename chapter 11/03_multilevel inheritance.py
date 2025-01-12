class Employee:
    a = 1

class Programmer(Employee): # Note : It inherit the attribute of class Employee and become a derived programmer class
    b = 2

# Multilevel inheritance : 

class Manager(Programmer): # Note : It inherit th attribute of derived class Programmer 
    # Meaning : (It inherit all attribute of both class Programmer as well as class Employee)
    c = 3

object_1 = Employee()
print(object_1.a) # It prints the value of (a) as it is present in the class Employee itself
print(object_1.b) # It gives the error as value b is not present in class Employee

object_2 = Programmer()
print(object_2.a) # It prints the value of (a) as we inherit the attibute and property of class Employee
print(object_2.b) # It prints the value of (b) as it present in class Programmer itself
print(object_2.c) # It gives an error because value of (c) is not present in class Programmer

object_3 = Manager() 
print(object_3.a) # It prints the value of (a) as it inherited the drived class Programmer which already inherited class Employee
print(object_3.b) # It prints the value of (b) as it inherited the class Programmer
print(object_3.c) # It prints the value of (c) as it present in the class Manger itself

