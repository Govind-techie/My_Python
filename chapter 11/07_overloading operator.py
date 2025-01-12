class Number:
    def __init__(self,n):
        self.n = n
        
    def __add__(self,num):
        return self.n + num.n
    
    def __sub__(self,a):
        return self.n - a.n
    
    def __mul__(self,b):
        return self.n * b.n
    
    def __truediv__(self,c):
        return self.n / c.n
    def __floordiv__(self,c):
        return self.n // c.n
        

a = Number(1)
b = Number(2)

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)







        