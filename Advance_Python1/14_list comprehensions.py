# List Comprehension : It is method to create a new list from the existing one through iteration with different conditions.

list_1 = [2,3,4,5,6,7]

squaredlist = []

for i in (list_1):
    squaredlist.append(i**2)

print(squaredlist)

# This code can written using list comprehensions.

squaredlist = [i**2 for i in (list_1)]
print(squaredlist)