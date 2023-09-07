class Person:

    #class attribute
    attr1 = 'Human'

    # instance attribute
    def __init__(self, name):
        self.name = name
    
# object instatiation
Sanbaj = Person('Sanbaj')
Samir = Person('Samir')

# Accessing class attributes
print(Sanbaj.name)
print(Sanbaj.attr1)
print(Sanbaj.__class__.attr1)