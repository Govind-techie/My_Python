# 1. Write a program using functions to find greatest of three numbers.

def greatest_number(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c


a = int(input("Enter your no. : "))
b = int(input("Enter your no. : "))
c = int(input("Enter your no. : "))

print(greatest_number((a),(b),(c)))
