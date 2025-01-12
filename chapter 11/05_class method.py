class Class_Method:
    a = 1 
    @classmethod
    def function_1(cls):
        print(f"The class attribute is {cls.a}")

object = Class_Method()
object.a = 2
object.function_1()