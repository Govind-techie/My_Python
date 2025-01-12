# Encapsulation : Bundling of data (attributes) and methods (functions) that operate on the data into a single unit (object), or a class. 

# Here, different attributes and functions are encapsulated in a single class.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

        @staticmethod # It converts a function with self parameter into a function which does not requires a self parameter.
        def hello(): 
            print("Hello")

    
    def get_percentage(self):
        total_marks = 0
        for mark in self.marks:
            total_marks += mark
        percentage = (total_marks/300) * 100
        return percentage


object_1 = Student("Govind Choudhary", [94, 94, 96])
total_percentage = object_1.get_percentage()

print(f"The student name is {object_1.name} who got {total_percentage} percentage in 10th boards")