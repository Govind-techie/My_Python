a = int(input("Enter 1st no. : "))
b = int(input("Enter 2nd no. : "))

if b == 0:
    raise ZeroDivisionError ("Denominator cannot be zero !!")
else:
    print(f"The division of {a}/{b} = {a/b}")
