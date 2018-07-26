"""
Working with pytest fixtures
run tests from terminal with 'py.test -s test_case_demo2.py'
"""

import pytest

@pytest.yield_fixture()
def setUp():
    print("\nRunning demo2 setup")
    yield # Before yield executes before method, after yield is after the method
    print("\nRunning demo2 teardown")

def test_methodA(setUp):
    print("Running demo2 method A")

def test_methodB(setUp):
    print("Running demo2 method B")

