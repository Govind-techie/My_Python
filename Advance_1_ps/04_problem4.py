# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by
# handling the ‘ZeroDivisionError’.

a = int(input("Enter the 1st no. : "))
b = int(input("Enter the 2nd no. : "))

if b == 0:
    raise ZeroDivisionError ("This division will carry on for infinite times.")
else:
    print(f"The value of {a}/{b} is {a/b}")