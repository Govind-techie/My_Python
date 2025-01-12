class hello:
    a = 1

b = hello()
b.a = 0 # It is an instance attribute
print(b.a) # here it prints the value of instance attribute rather than class attribute due to instance attribute have higher preference
print(hello.a) # when we print the class attribute it the value assign to class attribute does not change

# Ans : the answer is no as it only prints the instance attribute due to its higher preference and does not change the class attribute value