"""
Range creates a sequence of numbers,
but doesn't save them in memory
Useful for generating numbers
"""

# list() casts the range() to a list. Range generates numbers between 1st arg and 2nd arg
print(list(range(0, 10)))

a = range(5, 21)
print(a)
print(type(a))
print(list(a))

print("*" * 20)
b = range(10) # Prints 0-9
print(list(b))
b = range(2, 10) # Prints 2-9
print(list(b))
b = range(0, 10, 3) # Prints 0-9 in steps of 3
print(list(b))

print("*" * 20)
for num in range(4, 13, 4):
    print(num)