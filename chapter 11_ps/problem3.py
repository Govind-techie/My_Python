class employee:
    salary = 1000
    increment = 200

    @property
    def salaryafterincrement(self):
        
        return (self.salary + self.salary * (self.increment/100))
    
    @salaryafterincrement.setter
    def salaryafterincreament(self,salary):
    
        self.increment = ((salary/self.salary) - 1) * 100

# Formula :
 
# salaryafterincrement = salary + (increment/100)
# increment = (salaryafterincrement - salary) * 100

a = employee()
print(a.salaryafterincrement)


       
     
    


