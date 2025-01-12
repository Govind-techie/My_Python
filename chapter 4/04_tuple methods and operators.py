a = (1,34,34,"govind","mahesh","rakesh",78.89)

count = a.count(34) # count method gives the count of how many time a particular value of is appeared in a given tuple 
print(count) # we have to store the count we got using (count method) in seperate variable 

index = a.index("goivnd") # index method gives the index value of a particular value in tuple
print(index) # we have to store the index value we got using (index method) in seperate variable

print(len(a)) # length method print the total length of tuple 

# TUPLE OPERATORS

# Concatenation Operators (+)

b = (1, 2, 3) 
c = (4, 5, 6)
concatenate = b + c # concatenate operator used by using a (+) sign in between the 2 variable in which we stored tuple value 
print(concatenate)  # we have to store the concatenated value we got using (concatenate operator) in a different variable 

# Repetation Operators (*)

d = (1, 2, 3)
repetation = d * 3 # repeation operator used by using a (*) sign after variable and how many time we want to repeat the tuple
print(repetation)  # we have to store the repeated value we got using (repetation operator) in a different variable 

# Membership Operators (in /not in)

e = (1, 2, 3)
print(2 in e)     # membership operator checks whether the value in given tuple is present or not by using (in) or (not in)
print(4 not in e) # membership operator checks whether the value in given tuple is present or not by using (in) or (not in)

# Slicing Operators ([:])
 
f = (1, 2, 3, 4, 5)
slicing = f[1:4] # slicing operator extract a given portion of given tuple by using [:] sign
print(slicing)  # we have to store the sliced value we got using (slicing operator) in a different variable 

# Comparison Operators (==, !=, <, <=, >, >=)

g = (1, 2, 3)
h = (1, 2, 4)
print(g == h)  # comparison operator compare  all the value of given tuple with respect to same index
print(g < h)   # comparison operator compare  all the value of given tuple with respect to same index

# Minimum Operators 

i = (3, 1, 4, 1, 5, 9)
smallest = min(i) # minimum operator gives the smallest value of a given tuple 
print(smallest)  # we have to store the minimum value we got using (minimum operator) in a different variable 

# Maximum Operator

j = (3, 1, 4, 1, 5, 9)
largest = max(j) # maximum operator gives the largest value of a given tuple
print(largest) # we have to store the maximum value we got using (maximum operator) in a different variable 

# Unpacking Operator

k = (1, 2, 3)
a, b, c = k # unpacking operator assign or store all the value of given tuple in a variable respectively to their index 
print(a)  
print(b) 
print(c) 