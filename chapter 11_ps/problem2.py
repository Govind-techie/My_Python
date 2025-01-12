class animals:
    
    def __init__(self,a):
        self.a = a

        
          
    

class pets(animals):
    
    def __init__(self,a,b):
        super().__init__(a)
        self.b = b
        
    
class dogs(pets):
    
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c = c 

        print(f"my most fav animal is {self.a} it can be considered as a very good {self.b} it can provide the best {self.c} for your house") 
    
object = dogs("dog","pet","security")


    

    
    
        

        