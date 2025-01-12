# 5. Write a program to find the maximum of the numbers in a list using the reduce function.

list_of_numbers = [1,2,3,4,5,66,78,544,98,15]

def maximum_number(a,b): # Here, we pass 2 parameter within a function as a and b.
    if a > b: # if a is greater. 
        return a # Return, value of a.
    return b # Else, return value of b.

from functools import reduce # Here, we import reduce using the functools module.

print(reduce(maximum_number,list_of_numbers)) # Here, reduce takes 2 element from the list parameters for the function and reduce the value
# until it reach the maximum value.
