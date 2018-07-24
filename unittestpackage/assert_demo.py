"""
https://docs.python.org/3/library/unittest.html#unittest.TestCase
"""

import unittest

class AssertDemo(unittest.TestCase):

    def test_assertTrueFalse(self):
        a = True
        self.assertTrue(a, "** Failure: Testing true, but 'a' is not True **")
        b = True
        self.assertFalse(b, "** Failure: Testing false, but 'b' is not False **")

    def test_assertNotEqual(self):
        a = "Test"
        b = "Test"
        self.assertNotEqual(a, b, msg="** Failure: Testing not equal, but 'a' is equal to 'b' **")


if __name__ == '__main__':
    unittest.main(verbosity=2)