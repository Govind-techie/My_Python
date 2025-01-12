# Sets



# PROPERTIES OF SETS

# 1. Sets are unordered => Element’s order doesn’t matter
# 2. Sets are unindexed => Cannot access elements by index
# 3. There is no way to change items in sets.
# 4. Sets cannot contain duplicate values.
# 5. Sets are Mutable.

# The main difference between set and dict is that in dict we store key value pairs but in set we store only values

a = { "a" : 1 , "b" : 2 , "c" : 3} # its a  dictionary contain key value pair
b = {1 ,2 ,3,"govind"} # its a set contain only value. Here , ("govind" is also consider as a value) in set.
print(type(a))
print(type(b))

# Note  :

c = {1,2,3,4,5,5,5,5} # Note : (repetition of a certain value is not allowed in set)
print(c) # it will only print (5) 1 time even there are 4 same values of it

# Note : program to make an empty set 

d = set() # we have to use set command and then use this () brackets it create an empty set
