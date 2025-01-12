# Type Defintion : In type definations we explictly define the datatype for each variable for convinience using (:) before variable.

a : int = 3 # Here, as we explicitly mention the type of value present in a variable.
b : int = "Govind" # Here, we mention a certain datatype explicitly for varaible even though the datatype of a diferent value can be stored.

print(type(a)) # Output : <class 'str'>

# Note : Type definations are used for convinience and does not change the datatype of a value in a variable.

# Example_1 :

def sum(num1 : int , num2 : int) -> int: # Here, we defined a function and also mention that num1 and num2 both parameter are int
    # Here, we can also define that the return value of the function after calling it is also an int and we define it using a (->) symbol.
    return num1+num2

print(sum(2,4))

# Exmaple_2 :

age : int = 16

def greetings(name : str) -> str: # We, use (->) symbol to define the type of return value of name variable is a str.
    return f"My name is {name} and I am a {age} old young Programming and AI enthusiast"

print(greetings("Govind"))



