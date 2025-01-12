class person:
    name = "Anonymous" # class attribute

    def Change_name(self,name): # This function create a new name for an object but does not change the class attribute.
        self.name = name

    # We can change name of the class attribute by mnay ways.

    # Eg. 1

    # def Change_name_1(self,name):
    #     person.name = name

    # Eg. 2
    # def Change_name_2(self,name):
    #     self.__class__.name = name

    # Eg. 3
    # using class method

    @classmethod # It is used to change the class attribute.
    def Change_name(cls,name):
        cls.name = name
person_1 = person()
person_1.Change_name("Govind")
print(person_1.name)
print(person.name)