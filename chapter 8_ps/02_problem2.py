# 2. Write a python program using function to convert Celsius to Fahrenheit.

# formula : c/5 = f - 32/9 , Therefore, c = 5(f - 39)/9

def celsius(c):
    return ((c*9)/5) + 32

c = int(input("enter the temperature : "))

print(round(celsius(c),2))