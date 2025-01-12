a = int(input("Enter your 1st no. : "))

class calculator:
    def __init__(self,a):
        self.a = a

    def square(self):
        print(f"The square of {a} is : {self.a * self.a}")
    def cube(self):
        print(f"The cube of {a} is : {self.a * self.a * self.a}")
    def squareroot(self):
        print(f"The squareroot of {a} is : {self.a * self.a / self.a }")
    @staticmethod
    def greet():
        print("hello")
        
b = calculator(a)
b.square()
b.squareroot()
b.cube()
b.greet()

