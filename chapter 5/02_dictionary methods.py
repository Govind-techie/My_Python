
a = {
    "govind" : 8104859725 ,
    "mamta didi" : 9867469731 ,
    "pramila didi" : 8591555467 ,
    "mahesh" : 7208581272 , 
    "list" : (1,2,3) # if we have to pair more than one value we have to assign all value in a bracket using (,)

}
# Length Method

print(len(a)) # lenght method prints the total length of a given dictionary

# Items Method

print(a.items()) # items method give all value of dict in form of list and particular key value pairs in form of tuple

# Keys Method

print(a.keys()) # keys method gives all the keys present in a given dictionary

# Values Method

print(a.values()) # values method give all the value pair assign with a key of given dictionary

# Update Method

a.update({"dad" : 7208938893}) # update method add a new key and pair value to the original dictionary because of (mutablity)
# to use update method we have to 1st create a () and inside it  have to use {} and then makes the changes it it 
print(a) # Note : we have to print the updated value seperately because it changes makes changes in (original dictionary)

# Get Method

print(a.get("govind")) # get method gives the value that assigned to keys and we have to provide the ("key")
print(a,get("mom")) # if a given key does not exist in a given dictionary then it return (none) datatype

# Differnce between print(a.get("mom")) and print(a["mom"])

print(a.get("mom")) # it prints (None)
print(a["mom"]) # it returns an (error)

# Clear Method

my_dict1 = {'a': 1, 'b': 2, 'c': 3}
my_dict1.clear() # clear method clears out the entire given dictionary and make it empty
print(my_dict1)  # Output: {}

# Copy Method

my_dict2 = {'a': 1, 'b': 2}
new_dict = my_dict2.copy() # copy method copies out the entire given dictionary and store it in a new variable 
print(new_dict)  # Output: {'a': 1, 'b': 2}

# Formkeys Method

keys = ['a', 'b', 'c'] # create a list 
new_dict = dict.fromkeys(keys , 0 ) # it converts list into dict and assign a given value to the keys present in that list
print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}

# Pop Method

my_dict3 = {'a': 1, 'b': 2}
value = my_dict3.pop('b', None) # pop method eliminate a given key and paired value to it we can print the eliminated key
print(value)  # Output: 2 # we can print the eliminated key
print(my_dict3)  # Output: {'a': 1}

# Popitem Method

my_dict4 = {'a': 1, 'b': 2}
item = my_dict4.popitem() # popitems method removes and returns the last inserted key-value pair as a tuple
print(item)  # Output: ('b', 2) # we can print the eliminated item
print(my_dict4)  # Output: {'a': 1}

# Setdefault

my_dict5 = {'a': 1}
value = my_dict5.setdefault('b', 2) 
print(value)  # Output: 2 # Returns the value of the specified key.
print(my_dict5)  # Output: {'a': 1, 'b': 2} # If the key does not exist, inserts the key with the specified value.