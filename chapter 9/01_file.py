file = open("file.txt") # open command gives the access to read the given data from the given file.
data = file.read() # read command read the entire data from the file.
# Note : (we have to store the data we read in another variable)
print(data) 
file.close() # close command close the file we open file (using open commmand)

