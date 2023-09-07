# a = lambda x: x * x
# print(a(3))
# print('Hello World')

# path = lambda o, d: "Origin: " + o + " - " + "Destination:" + d
# print(path("Cairo","London"))

# i_value = "apples"
# i_object = iter(i_value)

# while True:
#     try:
#         item = next(i_object)
#         print(item)
#     except StopIteration:
#         print('No more items to iterate over')
#         break

# def disp(a,b):
#     yield a
#     yield b

# result = disp(10, 20)
# print(result)
# print(type(result))
# lst = list(result)
# print(lst)
# print(type(lst))

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(4))

# class Person:
#     name = 'Hari'
#     occupation = 'Software Devleper'
#     networth = 10

#     def info(self):
#         print(f'{self.name} is a {self.occupation}')

# a = Person()
# a.name = "Shubam"
# a.occupation = "Accountant"
# a.info()

# info = {"Carla", 19, False, 5.9, 19}
# print(info)

# # Decorators
# def greet(fx):
#     def mfx(*args, **kwargs):
#         print("Good morning.")
#         fx(*args, **kwargs)
#         print("Thanks for using our funciton")
#     return mfx


# def hello_world():
#     print("Hello, World!")

# def sum(a,b):
#     print(a+b)

# greet(hello_world)()
# greet(sum)(4,5)

# import logging

# def log_function_call(func):
#     def decorated(*args, **kwargs):
#         logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
#         result = func(*args, **kwargs)
#         logging.info(f"{func.__name__} returned {result}")
#         return result
#     return decorated

# @log_function_call
# def my_function(a, b):
#     return a + b

# my_function()

# class MyClass:
#     def __init__(self, value):
#         self._value = value
    
#     def show(self):
#         print(f'Value is {self._value}')

#     @property
#     def ten_value(self):
#         return 10 * self._value
    
#     @ten_value.setter
#     def ten_value(self, new_value):
#         self._value = new_value/10
    
# obj = MyClass(10)
# obj.ten_value = 67
# print(obj.ten_value)
# obj.show()


# def get_largest_numbers(numbers, n):
#     numbers.sort()

#     return numbers[-n:]

# nums = [2,3,4,1,34,123,321,1]

# print(nums)
# largest = get_largest_numbers(nums, 2)

# print(nums)


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __add__(self, other):
#         # Define the behaviour of the + operator for Point Objects
#         new_x = self.x + other.x
#         new_y = self.y + other.y
#         return Point(new_x, new_y)
    
#     #Create two Point objects
# point1 = Point(1, 2)
# point2 = Point(4, 5)

#     #user the + operator to add two point Objects 
# result = point1 + point2

# print(result.x, result.y)

