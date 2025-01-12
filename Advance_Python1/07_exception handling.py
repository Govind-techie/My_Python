# Exception Handling : In exception handling it try a particular code and if it runs the except block would get ignore and if the code has an
# error (try block) it would run the code in the except block.

# Note : Excptional handling consist of 2 main keywords (try) and (except) .

try: # Here, we used try keyword which excute a particular code present in the try block.
    a = int(input("Enter a number : "))
    print(f"Entered number : {a}")
except: # If code has an error it would run the except block of code presnt in it.
    print("Enter a valid number")

# We can specify a particular error in the except block:

try: 
    a = int(input("Enter a number : "))
    print(f"Entered number : {a}")
except ValueError: # Here, we are specifically mentioning that if the error is a (ValueError) run the except block with ValueError.
    print("It is a value error")
except TypeError: # Here, we are specifically mentioning that if the error is a (TypeError) run the except block with TypeError.
    print("It is a type error")

