'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 x 1
factorial(1) = 3 x 2 x 1
factorial(1) = 4 x 3 x 2 x 1
factorial(1) = 5 x 4 x 3 x 2 x 1

Therefore,
for factoraial of n would be
factorial(n) = n x (n - 1) x (n - 2) x ...... 3 x 2 x 1

Therefore,
it can be modified as :
factorial(n) = n x factorial(n - 1)

for eg.
factorial(3) = 3 x factorial(3-1)
factorial(3) = 3 x 2 x 1
'''


def factorial(n):
    if(n == 1 or n == 0):
        return 1
    return n * factorial(n-1)

n = int(input("enter your no. : "))
print(f"factorial of given no. is : ",{factorial(n)})

    

