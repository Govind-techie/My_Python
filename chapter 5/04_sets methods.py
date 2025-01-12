# a = {1 ,2 ,3,"govind"}

# # Add Method
# a.add(4) # add method add a given value to a given set
# print(a) # we have to print the set with added value using (add method) seperately 

# # Length Method

# print(len(a)) # length method gives the total length of a given set

# # Remove Method

# a.remove(1) # remove method eliminate a given value form a given set
# print(a) # we have to print the set with eliminated value using (remove method) seperately 

# # Pop Method

# a.pop() # pop method eliminate a random value from a given set 
# print(a) # we have to print the set with eliminated value using (pop method) seperately  

# # Clear Method

# a.clear()
# print(a)

# Discard Method

my_set1 = {1, 2, 3}
my_set1.discard(2) # discard method removes a given element from a given set 
print(my_set1)  # Output: {1, 3}
my_set1.discard(5)  # Note : (if given element of a given set does not found it not return error unlike (remove method)

# Copy Method 

my_set2 = {1, 2, 3}
new_set1 = my_set2.copy() # copy method creates the same copy of a given set 
print(new_set1)  # we have to store the copied set into a seperate variable 

# Update Method 

my_set3 = {1, 2, 3}
my_set3.update({4, 5}) # update method Updates the set, adding elements from one or more sets (union)
print(my_set)  # Output: {1, 2, 3, 4, 5}

