# Class : class is a blank space where you can store your given data

class employee :
    # attribute of the given class
    language = "python"
    salary = 2500000

# Object : object is created to access the given data in the class 
# Note : we have to define the class of the object to which it belongs eg. a = employee()
a = employee()
a.name = "govind" # We can specifically define the attribute of a object which is known as instance attribute
a.language = "javascript" # Note : instance attribute have more preference over class attribute. output (javascript)
print(a.salary,a.name,a.language)

# Here name is the attribute of the Object (a) and language and salary are the attribute of class as they directly belongs to the class
