# 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.
x = int(input("Enter the direction for vector : "))
y = int(input("Enter the direction for vector : "))
z = int(input("Enter the direction for vector : "))

class Vector_2D:
    def __init__(self , i , j):
        self.i = i
        self.j = j

    def show(self):
            print(f"Here, the 2D_Vector direction is  {self.i}i and {self.j}j")

class Vector_3D(Vector_2D):
    
    def __init__(self , i , j , k):
        super().__init__(i,j)
        self.k = k
        print(f"Here, the 3D Vector direction is {self.i}i , {self.j}j , {self.k}k ")

a = Vector_2D(x,y)
a.show()

b = Vector_3D(x,y,z)





