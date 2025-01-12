
class employee :
    # attribute of the given class
    language = "python"
    salary = 2500000

 

    def getinfo(self): # Note : Self is a argument created in a function to store the attributes of class 
        print(f"the languge is : {self.language} and the salary is : {self.salary}")
    

a = employee()
a.name = "govind" 
a.language = "javascript"
a.getinfo() # in this step it check that in employee class the language and salary attribute is stored in self argument
a.greet()

