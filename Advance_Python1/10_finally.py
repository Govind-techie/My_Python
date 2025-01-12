# Finally : Finally command runs a code no matter what and it is mostly used with functions to run finally code whether the function returns
# a value or not.

def try_finally():
    try: 
        a = int(input("Enter a number : "))
        print(f"Entered number : {a}")
        return
    except ValueError: # Here, we are specifically mentioning that if the error is a (ValueError) run the except block with ValueError.
        print("It is a value error")
        return
    except TypeError: # Here, we are specifically mentioning that if the error is a (TypeError) run the except block with TypeError.
        print("It is a type error")
        return
    finally:
        print("runs finally")

try_finally()
