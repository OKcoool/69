class Human:
    __age = 0
    __name = ""
    __lastname = ""
    __family = ""

    # public variables
    def get_age(self):  # getter for the age
        return self.__age

    # def set_age(self, value):  # setter for the age
    #   self.__age = value

    def get_name(self):  # getter for the name
        return self.__name

    # def set_name(self, value):  # setter for the name
    #   self.__name = value

    def get_lastname(self):  # getter for the lastname
        return self.__lastname

    # def set_lastname(self, value):  # setter for the lastname
    #   self.__lastname = value

    def get_family(self):  # getter for the family
        return self.__family

    # def set_family(self, value):  # setter for the family
    #   self.__family = value

    # constructor
    def __init__(self, name, lastname, age, family):
        self.__name = name
        self.__lastname = lastname
        self.__age = age
        self.__family = family

    def birthday(self):
        self.__age += 1

    def __str__(self):
        return f"{self.__name} {self.__lastname} ist {self.__age}"

    def marry(self, lastname):
        if self.__family == 'ledig':
            self.__family = 'married'
            self.__lastname = lastname
            return True
        else:
            return False
