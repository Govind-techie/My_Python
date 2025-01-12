# In list if a fuction is performed it changes the original list unlike strings which gives a new string with that function

a = ["govind","mamta didi",45,56.789,"mahesh",True,None]
print(a)
a.append("rakesh") # Append method put or assign a new value at the last index of list
print(a)

list1 = [1,2,34,56,54,78,22,46,12,90,7,7,7]

list1.sort() # sort method helps to sort the value a list in a given order

list1.sort() # it sort the given list of numbers in ascending order

list1.sort(reverse=True) # it sort the given list of numbers in descending order

print(list1)

list1.reverse() # reverse method helps to reverse the entire order of list and (print) or (return) its reverse order

print(list1)

list1.insert(5,89) # insert method help you to insert your value a given index in list

print(list1)

list1.pop(8) # pop method eliminate a particular value of list with given index of that value 

print(list1)

list1.pop() # if no index is metion for pop method it will consider last value or index of given list

print(list1)

print(list1.pop(8)) # it can also print the eliminated value of pop method with this program

list1.remove(56) # in remove method you need to give the exact value of list to eliminate it unlike pop which require index 

print(list1)

list1.clear() # clear method eliminate or clear all the value present in a given list although make the list empty

print(list1)

a = list1.count(7) # count method count a particular value of list that how many time it appears in given list 

print(a) # we have to store count of particular value in a seperate variable eg. a = list1.count(7)

b = list1.index(90) # index method gives the index of a particular value of a given list

print(b) # we have to store index count in seperate variable eg. b = list1.index(90) (it gives index value of 90 in list)

c = list1.copy() # copy method create a same copy of given list

print(c) # we have to store the copied list in a different variable eg. c = list1.copy()

d = len(list1) # length method gives the total length of list just like strings (length function)

print(d) # we have to store value of length in seperate variable
