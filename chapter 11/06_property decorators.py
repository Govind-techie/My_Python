class Property_Decorators:
    a = 1

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")
        self.lname = value.split(" ")
    
    
a = Property_Decorators()

a.fname = "Govind"
a.lname = "Choudhary"
print(a.name)