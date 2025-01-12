# Class : Class is a blue print of the object which means we store information of each object in the class

# Object : It is the instance of a class who's information is stored in it and we can extract that information from that object.

class student: # Here, is the class named student.

    # Here is the entire information of student class.

    name = "Govind Choudhary" # Name of student
    marks = 90 # Marks of student

object_1 = student() # Here, we defined an object of class student and the object contain all information stored in class student.

print(f"The student name is {object_1.name} who got {object_1.marks} percentage in 10th boards") # Here, we are extracting that information from that object.


class Car: # Here, we created a class named car.

    # Here, we stored details about the car
    Colour = "Red"
    Number_Of_Car = 15
    Brand = "Buggati"
    Model_Name = "Veyron"

Car_1 = Car() # Here, we created an object that has all the details of the car (Instance of class Car).

print(f"Car name is : {Car_1.Brand} {Car_1.Model_Name}")
print(f"Colour of car is : {Car_1.Colour}")
print(f"Rarity of Car : There only total of {Car_1.Number_Of_Car} cars in the entire world")