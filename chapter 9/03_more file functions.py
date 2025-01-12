# Readline Function

# Note : readline is a function read a given line 1 by 1 and gives the output in form of (string)

file = open("file.txt")

line = file.readline()
print(line,type(line))

line2 = file.readline()
print(line2,type(line2))

line3 = file.readline()
print(line3,type(line3))

line4 = file.readline() # Note : If the given line does not exist in a given file then it prints nothing
print(line4 == "") # This step shows that line4 which does not exist in the given file is an empty string and return true

file.close()

# same program using loops
line = file.readline()
while(line != ""):
    print(line)
    line = file.readline()



#  Readlines Function

# Note : readlines function print all lines at the same time and gives the output in the form of (list)

file2 = open("file.txt")
line = file2.readlines() # readlines function read multiple line at the same time
print(line,type(line)) # it gives the output in the form of list type
file2.close()

# Difference in (readline function) and (readlines function)

# 1. readline function print 1 line at a given time whereas readlines function read multiple line at the same time
# 2. readline function gives the output in the form of string whereas readlines gives the output in the form of list
