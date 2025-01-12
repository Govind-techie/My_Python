# Super method : The super() function is used to give access to the methods and properties of a parent or sibling class.
# The super() function returns a temporary object of the parent class.

class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("Car Started")

    @staticmethod
    def stop():
        print("Car Stopped")
    
class Toyota_Car(Car):

    def __init__(self,name,type):
        super().__init__(type)
        self.name = name
        super().start()

car_1 = Toyota_Car("Fortuner","Petrol")
print(car_1.type)

