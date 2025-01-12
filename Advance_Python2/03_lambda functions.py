# Lambda Functions : Lambda is function with parameters and an expression which create that particular variable as a function.

# Lambda Functions Sturcture : (Variable) = lambda (parameter) : (expression)

# To print square of a number.

# Function without lambda :

def square(x):
    return x*x

print(square(5))

# Lambda function :
square = lambda x : x*x # Here, we created a variable as square with lambda with the parameters as x followed by a (:) and the expression to return.
print(square(5)) # Here, we use the name of the variable which has became a function using lambda and prints its return value.

# Examples : To print the sum of three numbers.

sum = lambda a,b,c : a+b+c # Here, we take three parameters and then the sum expression.
print(sum(3,4,5)) # Here, we print the total sum of the numbers.