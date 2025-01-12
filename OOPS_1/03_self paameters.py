# Self Parameter : self is a convention in Python that refers to the instance of a class.


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def get_percentage(self):
        total_marks = 0
        for mark in self.marks:
            total_marks += mark
        percentage = (total_marks/300) * 100
        return percentage


object_1 = Student("Govind Choudhary", [94, 94, 96])
total_percentage = object_1.get_percentage()

print(f"The student name is {object_1.name} who got {total_percentage} percentage in 10th boards")