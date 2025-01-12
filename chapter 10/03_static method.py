
class employee :
    # attribute of the given class
    language = "python"
    salary = 2500000

    @staticmethod # staticmethod indicates that we don't need any particular argument for a given function
    def greet(): 
        print("good morning")

a = employee()
a.name = "govind" 
a.language = "javascript"
a.getinfo() # in this step it check that in employee class the language and salary attribute is stored in self argument
a.greet()

