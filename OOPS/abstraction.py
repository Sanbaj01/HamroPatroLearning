# class MyClass:

#     # Hidden member of MyClass
#     __hiddenVariable = 0

#     # A member method that changes 
#     # __hiddenVariable
#     def add(self, increment):
#         self.__hiddenVariable += increment
#         print(self.__hiddenVariable)

# # Driver code
# myObject = MyClass()
# myObject.add(2)
# myObject.add(5)

# # This line causes error
# print (myObject._MyClass__hiddenVariable)

class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __repr__(self):
        return "Test a:%s b:%s" % (self.a, self.b)
    
    def __str__(self):
        return "From str method of Test: a is %s," \
            "b is %s" % (self.a, self.b)
# Driver code
t = Test(1234,5678)
print(t) # This calls __str__()
print([t]) # This calls __repr__()