"""
Creating your own modules
"""

# Import the module... it is inefficient to import the whole module if not needed
import math
# Importing only what you need
from math import sqrt

## Importing my own module
# import module_external.car as car
## Better way of importing whole module
# from module_external import car
# Import specific method from car module
from module_external.car import info

class ModulesDemo():

    def builtin_modules(self):
        # Use imported math module to get the square root of 100
        print(math.sqrt(100))
        # When "from" is used, you do not need the module name before the function
        print(sqrt(100))

    def car_description(self):
        # Method that uses my "car" external module
        make = "BMW"
        model = "550i"
        # Module is imported as car, so access the module methods with "car." when whole module is imported
        # car.info(make, model)
        # When specific method is imported, omit module name
        info(make, model)


# Instantiate class
m = ModulesDemo()
# Call class method
m.builtin_modules()
# Call class method that uses my external module
m.car_description()