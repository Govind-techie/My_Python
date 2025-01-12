# 3. Write a list comprehension to print a list which contains the multiplication table of a
# user entered number.

a = int(input("Enter the no. : "))

table = [a*i for i in range(1,11)]
print(table)