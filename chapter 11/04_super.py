class Employee: # Super Class for Class Programmer
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee): # Super Class for Class Manager
    def __init__(self):
        super().__init__()
        print("Constructor of Programmer")
    b = 2



class Manager(Programmer):
    def __init__(self):
        super().__init__() # Super method run the init function of the previous class Programmer including it also run the init function of class manager
        print("Constructor of Manager")
    c = 3

a = Employee()

b = Programmer()


c = Manager()

