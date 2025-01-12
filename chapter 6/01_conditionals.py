# Conditional Expression : (if , else , elif)

a = int(input("enter your age : "))

# This is called as if , elif , else ladder

# if statement :

if(a>=18): # (if) checks the given condtion and if it True it execute the function in it and if False it moves to next condition
    print("you are eligible to amke a driving license sir")

# elif statement : we use it when we ahve to write more conditions then (if and else) statement

elif(a<0): # (elif) checks the given condtion and if it True it execute the function in it and false then jumps to next condition
    print("age cannot be negative its invalid")

elif(a==0):# (elif) checks the given condition if it is True it excute the function in it and false then jumps to next condition
    print("you are entering 0 age which does not count as an age")
    
# else statement :

else : # (else) checks the given condition excute the function in it and then the program ends 
    print("sorry sir !!")
    print("you are eligible to amke a driving license sir")

print("end of Program")

# IMPORTANT NOTES:
# 1. There can be any number of elif statements.
# 2. Last else is executed only if all the conditions inside (if) and (elifs) fail.

# Structure of if else and elif conditon and their working

# if (condition1): # if condition1 is True
# print ("yes")

# elif(condition2): # if condition2 is True
# print("no")

# else: # otherwise
# print("maybe")