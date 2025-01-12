class programmer:
    company = "microsoft"

    def __init__(self,name,language,salary):
        self.name = name
        self.language = language
        self.salary = salary
        
a = programmer("govind","javascript",2500000)
print(a.name,a.language,a.salary)