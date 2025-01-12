# Polymorphism : Polymorphism is the ability of an object to take on many forms.

# In Python, polymorphism is achieved through method overriding and method overloading.

# Method overriding : Method overriding is a feature of object-oriented programming where a subclass provides a specific implementation of a method 
# that is already defined in its parent class.

# Operator overloading : Operator overloading is a feature of object-oriented programming where a method is defined to override the behavior of an operator.

# Dunder methods : Dunder methods are special methods in Python that start and end with double underscores (e.g., __init__, __str__, __add__).
# They are used to define special behaviors for objects.

# Example :

class ComplexNumber:
    # Constructor to initialize a complex number with real and imaginary parts
    def __init__(self,real,imaginary):
        self.real = real          # Real part of complex number
        self.imaginary = imaginary # Imaginary part of complex number

    # Method to display the complex number in the form ai + bj
    def ShowNumber(self):
        print(f"{self.real}i + {self.imaginary}j")

    # Operator overloading for addition (+)
    # This method is called when we use + operator between two ComplexNumber objects
    def __add__(self,number_2):
        new_real = self.real + number_2.real           # Add real parts
        new_imaginary = self.imaginary + number_2.imaginary # Add imaginary parts
        return ComplexNumber(new_real,new_imaginary)    # Return new complex number
    
    # Operator overloading for subtraction (-)
    # This method is called when we use - operator between two ComplexNumber objects
    def __sub__(self,number_2):
        new_real = self.real - number_2.real           # Subtract real parts
        new_imaginary = self.imaginary - number_2.imaginary # Subtract imaginary parts
        return ComplexNumber(new_real,new_imaginary)    # Return new complex number


# Creating first complex number object (1 + 2j)
number_1 = ComplexNumber(1,2)
number_1.ShowNumber() 

# Creating second complex number object (3 + 4j)
number_2 = ComplexNumber(3,4)
number_2.ShowNumber()

# Adding two complex numbers using overloaded + operator
number_3 = number_1 + number_2    # This calls __add__ method
number_3.ShowNumber()

# Subtracting two complex numbers using overloaded - operator
number_4 = number_1 - number_2    # This calls __sub__ method
number_4.ShowNumber()