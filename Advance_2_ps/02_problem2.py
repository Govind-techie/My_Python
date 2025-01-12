# 2. Write a program to input name, marks and phone number of a student and format it using the format function like below:

# “The name of the student is Harry, his marks are 72 and phone number is 99999888”

# Here, we take the necessary input from user:

name = input("Enter your name : ")
marks = int(input("Enter your marks : "))
phone_number = int(input("Enter your phone number : "))

# Here, we use format method (old way):

print("The name of the student is {1}, his marks are {0} and phone number is {2}".format(marks,name,phone_number))
# Note : In format method we can mention the index in the curly braces ({index}) to store the variable inforamtion accordingly.

# F string (new way):

print(f"The name of the student is {name}, his marks are {marks} and phone number is {phone_number}")
