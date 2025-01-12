# Enumerate Function : The enumerate function is used to get index of the element each time it iterate over the element of a list,tuple,dict.

list_1 = [1,45,6,7,8,9]

# To print the index and the element fo the list.

# Without Enumerate :

index = 0
for i in (list_1):
    print(f"The number a index {index} is {i}")
    index += 1

# With Enumerate :

for index,i in enumerate(list_1):
    print(f"The number a index {index} is {i}")