# Operations in Sets

set1 = {1 , 2, 3 , 4 , 5}
set2 = {1 , 6 , 5, 8 ,}

# Union Method

print(set1.union(set2)) # union method combine 2 given sets and the common value between 2 given sets is printed only (1 time)

# Intersection Method

print(set1.intersection(set2)) # intersection method gives the common value between 2 given sets

# Difference

set3 = {1, 2, 3}
set4 = {3, 4, 5}
result = set3.difference(set4) # difference method gives the different element of set3 with respect to set4
print(result)  # Output: {1, 2} # we have to store the different value we got in a seperate variable

# Symmetric Difference

set5 = {1, 2, 3}
set6 = {3, 4, 5}
result = set5.symmetric_difference(set6) # symmetric difference gives all the different element present in both given set
print(result) # Output: {1, 2, 4, 5} # we have to store the different value we got in a seperate variable

# isdisjoint

set7 = {1, 2, 3}
set8 = {4, 5, 6} # isdisjoint returns True if the set has no elements in common with another set
print(set7.isdisjoint(set8))  # Output: True

# issubset

# Note : subset means, if a small set contains all same element of a larger set then it is called the subset of larger set

set9 = {1, 2}
set10 = {1, 2, 3} # issubset returns True if the set is a subset of another set 
print(set9.issubset(set10))  # Output {True}

# issuperset

# Note : superset means, if a large set contains all same element of a small set then it is called the superset set of small set

set11 = {1, 2, 3}
set12 = {1, 2} # issuperset returns True if the set is a superset of another set
print(set11.issuperset(set12))  # Output: True
