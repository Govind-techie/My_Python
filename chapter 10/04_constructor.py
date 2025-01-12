
class employee :
    # attribute of the given class
    language = "python"
    salary = 2500000

    # (_init_) is a dunder method which calls a given function automatically whenever an object is created
 
    def __init__(self , name , salary , language): # We can create a variable in the (_init_) and then we can assign instance attribute accordingly
        self.name = name
        self.language = language
        self.salary = salary
        print ("I am creating an object") 

    

    

a = employee("govind","javascript",3000000) # We are assigning the given value to the variable in mentioned in the (_init_) 
print(a.name,a.language,a.salary)

