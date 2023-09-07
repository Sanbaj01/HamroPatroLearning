# class Person(object):
#     def __init__(self, name, idnumber):
#         self.name = name
#         self.idnumber = idnumber
#     def display(self):
#         print(self.name)
#         print(self.idnumber)
    
#     def details(self):
#         print(f"My name is {self.name}.")
#         print(f'IdNumber: {self.idnumber}.')

# class Employee(Person):
#     def __init__(self, name, idnumber, salary, post):
#         self.salary = salary
#         self.post = post

#         #invoking the __init__ of the parent class
#         Person.__init__(self, name, idnumber)
#     def details(self):
#         print(f'My name is{self.name}.')
#         print(f'IdNumber: {self.idnumber}')
#         print(f'Post: {self.post}.')
    
# a = Employee('Sanbaj', 406, 15000, "Fellow")
# a.display()
# a.details()

