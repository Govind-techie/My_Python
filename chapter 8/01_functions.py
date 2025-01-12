# Function

# A function is a group of statements performing a specific task.
# When a program gets bigger in size and its complexity grows, it gets difficult for
# program to keep track on which piece of code is doing what!
# A function can be reused by the programmer in a given program any number of time he want to


# a = int(input("enter your no. : "))
# b = int(input("enter your no. : "))
# c = int(input("enter your no. : "))

# average = (a+b+c)/3
# print(average)

# if want to repeat the same program 5 times we can do it like this :

# Function Defination̦ : The part containing the exact set of instructions which are executed during the function call.



def avg():
    a = int(input("enter your no. : "))
    b = int(input("enter your no. : "))
    c = int(input("enter your no. : "))

    average = (a+b+c)/3
    print(average)
    return avg()
# now to perform same program multiple time we have to write the name of function to which the given program is assign
# Note : avg() is a function name



# Function Call : Whenever we want to call a function, we put the name of the function followed by parentheses as follows


a = avg() # Function Call
print("thanks")
avg() # Function Call
print("thanks")
avg() # Function Call
print("thanks")
avg() # Function Call
print("thanks")
avg() # Function Call
print("thanks")