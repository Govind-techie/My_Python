a = "govind" 

file = open("file2.txt" , "w") # In this step it create a new file with write mode ("w")
file.write(a) # write command write a given data store in a given variable in a file mentioned in the open commmand
file.close() 

# Note : Write argument takes the input and write in the new file only when the given data in the variable is in (string) datatype

# Note : write and read are two type of function for file