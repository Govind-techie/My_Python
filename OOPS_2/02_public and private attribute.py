# Public Attribute : Generally, attribute are already puclic and can be accessed outside the class directly.
# Private Attribute : Private attribute is defined with double underscore(__) before the attribute name. It can't be accessed directly outside the class.
class Account:
    def __init__(self,name,account_number,password):
        self.name = name
        self.account_number = account_number
        self.__password = password # Here, __password is a private attribute of the class.

    def get_password(self):
        print(self.__password)

    def __hello(self): # Here, __hello is a private function of the class.
        print("Hello")

account_1 = Account("ABC",12345,"abcd")
print(account_1.name) 
print(account_1.account_number)
# print(account_1.__password) # Here, we can't access the private attribute __password because it is defined outside the class.
print(account_1.get_password()) # Here, we can access the private attribute __password by using a method because the function get_password() is within the class.
# print(account_1.__hello()) # Here, we can't access the private method __hello() because it is defined outside the class.