# 4. Write a program to filter a list of numbers which are divisible by 5.

list_of_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] # Here, is the list of numbers

# Function that see the number is divisible of 5 or not.

divisible_by_5 = lambda x : x%5 == 0 # Here, we created a lambda function which checks whether a no. is 5 divisible and return (True) or (False).

print(list(filter(divisible_by_5,list_of_numbers))) # Filter pass each element of list as parameter of function and prints the 5 divisible which is true.


