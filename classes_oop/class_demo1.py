"""
Object-Oriented Programming
"""

class Car(object):
    # This is required for classes, initializes all objects from this class, basically a constructor
    def __init__(self, make, model='550i'):
        self.make = make
        self.model = model

# Create instance of class
c1 = Car('BMW')
c2 = Car('Mazda')

print(c1.make)
print(c1.model)
print(c2.make)

c2.make = 'Honda'

print(c2.make)
