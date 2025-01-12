# Write a program to print third, fifth and seventh element from a list using enumerate function.

list_1 =  [2,4,6,7,8,9,0,12,14,13] # Here, we created a list of numbers.



for index,item in enumerate(list_1): # Here we ieterate over a list of element 
    if index in (3,5,7) : # Here, we put a condition that the index is in (3,5,7)
        print(f"The number at index {index} is {item}") # if index is (3,5,7) it will print the index along with element.




