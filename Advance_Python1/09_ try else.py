# Try else : when we use try and except method we can also add an else statement and it will run only if the try block code does not have an error.

try: # Here, we used try keyword which excute a particular code present in the try block.
    a = int(input("Enter a number : "))
    print(f"Entered number : {a}")
except: # If code has an error it would run the except block of code presnt in it.
    print("Enter a valid number")

else: # Here, else statement will only run if the try block runs.
    print("Hurray, no error")