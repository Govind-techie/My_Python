class Student:
    def __init__(self,phy,chem,maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        

    # def percentage(self):
    #     self.percentage = (str((self.phy + self.chem + self.maths)/3) + "%")

    @property
    def percentage(self):
        return (str((self.phy + self.chem + self.maths)/3) + "%")


student_1 = Student(80,90,100)
print(student_1.percentage)

student_1.phy = 75
print(student_1.phy)
print(student_1.percentage)