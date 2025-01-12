# 4. Write a recursive function to calculate the sum of first n natural numbers.

'''
sum(n) = 1 + 2 + 3 + ......n
sum(5) = 1 + 2 + 3 + 4 + 5
Therefore,
sum(n) = (n - 1) + n
'''

def sum(n):
    if(n == 1):
        return 1
    return sum(n - 1) + (n)

n = int(input("Enter your no. : "))

print(sum(n))