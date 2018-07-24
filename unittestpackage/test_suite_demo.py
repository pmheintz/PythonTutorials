"""
Creating a test suite combining test_class1 and test_class2
"""

import unittest
# Import additional classes to use
from test_class1 import TestClass1
from test_class2 import TestClass2

# get all tests from test class 1 & 2
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestClass1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestClass2)

# create a test suite combining TestClass1 and TestClass2
build1_test = unittest.TestSuite([tc1, tc2])

# run the test suite
unittest.TextTestRunner(verbosity=2).run(build1_test)