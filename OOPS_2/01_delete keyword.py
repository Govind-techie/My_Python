# Delete Keyword : Delete keyword used to delete the instance attribute or an entire object of a class.

class student:

    def __init__(self,name,roll_number):
        self.name = name
        self.roll_number = roll_number

    
student_1 = student("Govind",5)
print(student_1.name) # Here, it will print the name because object is deleted after the code is executed.
del student_1.name # It will delete the name attribute of object student_1.
# print(student_1.name) : It will raise an error that the object attribute doesn't exist.
del student_1 # It will delete the entire object student_1.







