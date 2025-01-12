# Abstraction : Abstraction means hiding complex details and showing only the necessary features. 

class Car:

    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start_car(self):
        self.clutch = True 
        self.acc = True

# Here, we dont's showcase that to start the car we need to push clutch and accelerator in ordr to start it when we start a car it automatically gets true.

        print("Car Started")

car_1 = Car()
car_1.start_car()
