file = open("file.txt") 
data = file.read() 
print(data) 
file.close()

# The same program can be written as :

with open("file.txt") as file:
    print(file.read())

# In this program you dont have to close the file. 

