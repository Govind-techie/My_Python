# Map Function : Map is used to run a particular function on each element of a list,tuple,dict.

# Map Example : 

list_of_numbers = [1,2,3,4,5,6] # Here, is the list of numbers.

square = lambda x : x**2 # Here, we created a function using lambda.

# Note it is not neccessary that a function has to be a lambda function.

squaredlist = map(square,list_of_numbers) # Here, map is taking every element of list as parameter for square function and returning the value

print(squaredlist) # It prints the representation of map object.(Output : <map object at 0x1007f5ae0>)
print(list(squaredlist)) # Here, we mentioned that we have to print it in the form of list. (Output : [1, 4, 9, 16, 25, 36])

# Filter Function : Filter function run a particular function on each element of list,tuple,dict and it will filter out the value if its true
# and does not print is the value is false

# Filter Example :

list_of_numbers = [1,2,3,4,5,6] # Here, is the list of numbers.

def even_number(n): # Here, we created a function with paramter as n
    if n%2 == 0 :
        return True
    return False

# Same function in the form of lambda function : even_number = lambda n : n % 2 == 0

only_even = filter(even_number,list_of_numbers)

print(only_even) # It prints the representation of filter object.(Output : <filter object at 0x104269ed0>)
print(list(only_even)) # Here, we mentioned that we have to print it in the form of list. (Output : [2, 4, 6])

# Reduce Function :reduce function is part of the functools module and it is used to reduce a sequence of elements to a single value by applying
# a function cumulatively to the items of the iterable.

# Reduce Example :

from functools import reduce

list_of_numbers = [1,2,3,4,5,6] # Here, is the list of numbers.

sum = lambda a,b : a+b
print(reduce(sum,list_of_numbers))

# Reduce Breakdown : For (sum) function.

# •	Step 1: add(1, 2) → 3
# •	Step 2: add(3, 3) → 6
# •	Step 3: add(6, 4) → 10
# •	Step 4: add(10, 5) → 15
# •	Step 5: add(15, 6) → 21

mul = lambda x,y :x*y
print(reduce(mul,list_of_numbers))

# Reduce Breakdown : For (mul) function.

# •	Step 1: add(1, 2) → 2
# •	Step 2: add(2, 3) → 6
# •	Step 3: add(6, 4) → 24
# •	Step 4: add(24, 5) → 120
# •	Step 5: add(120, 6) → 720





