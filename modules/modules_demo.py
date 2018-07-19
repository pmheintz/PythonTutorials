"""
https://docs.python.org/3/library
"""

# Import the module... it is inefficient to import the whole module if not needed
import math
# Importing only what you need
from math import sqrt

class ModulesDemo():

    def builtin_modules(self):
        # Use imported math module to get the square root of 100
        print(math.sqrt(100))
        # When "from" is used, you do not need the module name before the function
        print(sqrt(100))


# Instantiate class
m = ModulesDemo()
# Call class method
m.builtin_modules()