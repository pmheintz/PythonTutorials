"""
Some built in functions, best used on numbers
max() -> Takes a number of args and returns the largest one
min() -> Takes a number of args and returns the smallest one
abs() -> Takes one arg and returns the absolute value (distance from 0)
type() -> Returns the data type of an argument
"""

def largest_num(*args):
    print(max(args))

largest_num(-20, -10, 0, 10, 100)

def smallest_num(*args):
    print(min(args))

smallest_num(-20, -10, 0, 10, 100)

def absolute_value(num):
    print(abs(num))

absolute_value(-9)

l = [1, 2, 3]
t = (1, 2, 3)
d = {'one': 1, 'two': 2, 'three': 3}
print(type(99))
print(type(99.1))
print(type("99.1"))
print(type(True))
print(type(l))
print(type(t))
print(type(d))