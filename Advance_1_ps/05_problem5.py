# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.

a = int(input("Enter the no. : ")) # Here, we take a number as an input from integer.

table = [a*i for i in range(1,11)] # Here, we store the table in a list using list comprehensions.

with open("Tables.txt" , "a") as f: # By, using context manager we open the file and and use append method using "a"
    f.write(f"Table of {a} is {table}\n") # Here, we write the list of tables in tables.txt by appending it into that file.

# Note : if we use "w" (write) method we can write the table in the file but it will not store the previous table we write in that file.
# Note : Here, we use "a" (append) method we can append the table in the file and it will store the previous table we write in that file.