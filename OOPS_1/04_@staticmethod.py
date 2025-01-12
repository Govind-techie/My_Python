# @staticmethod : A static method is a method that belongs to a class rather than an instance of the class. It doesn't require a self parameter 
# and can't access or modify class state or instance state directly.

class Hello:
    
    # staticmethod functions works on class level.

    @staticmethod # It converts a function with self parameter into a function which does not requires a self parameter.
    def hello(): 
        print("Hello")


object = Hello()
object.hello() 

# Note : @staticmethod is a decorator.


