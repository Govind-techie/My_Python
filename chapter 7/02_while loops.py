# While Loop 

# imp:

# In while loops, the condition is checked first. If it evaluates to true, the body of the loop
# is executed otherwise not!

# If the loop is entered, the process of [condition check & execution] is continued until
# the condition becomes False.

i = 1

while(i<6): 
    print(i) # Here , we print (i)
    i += 1 # in this step we incrementing the value of i variable by 1 till it satisfy the condition as False

# Note : In while loop we don't need to specify the range like for loops

# Output :
# 1    
# 2
# 3   
# 4
# 5
# it does not print 6 because we gave condition (1<6) and not (i<=6)