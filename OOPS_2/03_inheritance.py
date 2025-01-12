# Inheritance : Inheritance is a mechanism in which a class acquires the attributes and methods or functions of another class.

# Single Inheritance : In single inheritance, a subclass inherits the attributes and methods of a single superclass.

class Car:

    @staticmethod
    def start():
        print("Car Started")
    
    @staticmethod
    def stop():
        print("Car Stopped")

class ToyotaCar(Car): # Here, ToyotaCar class has inherited the attributes and methods of Car class.

    # In this class there is no need to define the start() and stop() methods again because they are inherited from Car class.
    brand = "Toyota"
        
ToyotaCar_1 = ToyotaCar()
ToyotaCar_1.start() # Here, we can access the start() method of Car class because ToyotaCar is a subclass of Car class.
ToyotaCar_1.stop() # Here, we can access the stop() method of Car class because ToyotaCar is a subclass of Car class.
print(ToyotaCar_1.brand) # Here, we can access the brand attribute of ToyotaCar class.

# Multilevel Inheritance : In multilevel inheritance, a subclass inherits the attributes and methods of a single superclass and then the subclass 
# itself becomes a superclass for another subclass.

class Fortuner(ToyotaCar): # Here, Fortuner class has inherited the attributes and methods of ToyotaCar class and Car class.
    def __init__(self,type):
        self.type = type

Fortuner_1 = Fortuner("Petrol")
print(Fortuner_1.start()) 
print(Fortuner_1.stop() )
print(Fortuner_1.type)
print(Fortuner_1.brand)

# Multiple Inheritance : In multiple inheritance, a subclass inherits the attributes and methods of multiple superclasses.

class A:
    variable_A = "welcome to class A"

class B:
    variable_B = "welcome to class B"

class C(A,B): # Here, C class has inherited the attributes and methods of A class and B class and the class is separated by comma.
    variable_C = "welcome to class C"

class_c = C()
print(class_c.variable_A)
print(class_c.variable_B)
print(class_c.variable_C)