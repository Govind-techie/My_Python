# 3. A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers.

table_7 = [str(7*x )for x in range(1,11)] # Here, we create a list of table of 7 using list comprehensions.
# Note : Here, we explicitly converted the list of table into string.

print("\n".join(table_7)) # Here, we join "/n" to each element of the list of tables in form of string which gives the new line to every element.

