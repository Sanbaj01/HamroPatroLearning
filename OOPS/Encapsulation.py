# Python program to demonstrate private members

# creating a Base class
class Base:
    def __init__(self):
        self.a = "GeekforGeeks"
        self.__c = "GeeksforGeeks"   # Private variables

# creating a derived class
class Derived(Base):
    def __init__(self):

        #calling constructor of Base Class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)

obj1 = Base()
print(obj1.a)
# ob2 = Derived()
# print(obj2.a)