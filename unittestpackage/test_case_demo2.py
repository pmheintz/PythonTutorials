"""
Class level unit tests
"""

import unittest

class TestCaseDemo(unittest.TestCase):

    # Setup something to run once before ALL tests
    @classmethod
    def setUpClass(cls):
        print("*" * 30)
        print("I will run only once before ALL tests")
        print("*" * 30)

    def setUp(self):
        print("I will run once before every test")

    # Important to start methods with "test"
    def test_methodA(self):
        print("Running method A")

    def test_methodB(self):
        print("Running method B")

    def tearDown(self):
        print("I will run after every test")

    # Setup something to run once before ALL tests
    @classmethod
    def tearDownClass(cls):
        print("*" * 30)
        print("I will run only once after ALL tests")
        print("*" * 30)

if __name__ == '__main__':
    unittest.main(verbosity=2)