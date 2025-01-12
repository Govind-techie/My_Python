# Walrus Operator : Walrus operator (:=) is used to assign values to the variable with an experessions as part of a condition.
# Note : Walrus Operator cna only be used only with a given conditions.

# Example_1 : Without using walrus operator.

n = len([1,2,3,4,5])

if n >= 3:
    print(f"This list is too long, because it contains {n} elements in it.") 

# Example_2 : Using walrus operator.

if (n := len([1,2,3,4,5])) >= 3: # Here, by walrus operator we can directly assign the len function directly to the varaible with the condition.
    print(f"This is list is too long, because it contains {n} elements in it.")

# Example_3 : More walrus operator.

if (length := len(data := input("Enter your name : "))) > 5: # Here, we use two walrus operation in one condition.
    print("Your name is too long ")

