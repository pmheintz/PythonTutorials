"""
Multiple ways to run test cases
file names should start with test
a test method name should start with test

py.test test_mod.py # run tests in module
py.test some_path # run all tests below some path
py.test test_module.py::test_method # only run test_method in test_module

-s to print statements
-v verbose
"""

import pytest

@pytest.yield_fixture()
def setUp():
    print("\nRunning demo 3 setup")
    yield
    print("\nRunning demo 3 teardown")

def test_demo3_methodA(setUp):
    print("Running demo 3 method A")

def test_demo3_methodB(setUp):
    print("Running demo 3 method B")