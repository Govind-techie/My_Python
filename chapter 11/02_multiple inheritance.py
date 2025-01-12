class Employee:
    Company = "Google"
    employee = "Govind"
    year = 2
    def show(self):
        print(f"The name of the employee is {self.employee} and he has the experience of {self.year} years in Microsoft")


class Coder:
    language = "Python"
    def printlanguages(self):
        print(f"Out of all languages , here is your language {self.language}")

# The Multiple Inheritance Class

class Programmer(Employee,Coder): # It ineherit the attribute of class Employee in class Programmer

    # Here, Class Employee is a base class and Class Programmer is a derived Class
    Company = "Microsoft"

    def resume(self):
        print(f"I have done {self.year} of experience at Microsoft as a SDE 2")
        print(f"I have a good knowledge and experience in {self.language} language")

a = Programmer()

# Note : we can create any instance attribute for object (a) and even there are two different class
# Note : when we make any change in the function of a particular class it will also inherit the changes done in the class fue to inheritence


a.show()
a.printlanguages()
a.resume()

