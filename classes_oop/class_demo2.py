"""
Object-Oriented Programming
"""

class Car(object):
    # Member variables
    wheels = 4

    # This is required for classes, initializes all objects from this class, basically a constructor
    def __init__(self, make, model='550i'):
        self.make = make
        self.model = model

    # Class method
    def info(self):
        print("Make of the car: " + self.make)
        print("Model of the car: " + self.model)

    ### End of class ###

# Create instance of class
c1 = Car('BMW', '550i')
# Not a good idea to access member variables directly
c1.wheels = 3
c2 = Car('Mazda', 'Speed 6')

c1.info()
print("Car class has " + str(Car.wheels) + " wheels.")
print("c1 car has " + str(c1.wheels) + " wheels.")
c2.info()
print("c2 car has " + str(Car.wheels) + " wheels.")
