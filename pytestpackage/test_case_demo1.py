"""
Using the new pytest framework
pip3 install pytest
py.test from terminal runs tests
py.test -v -s runs tests and prints statements regardless of whether or not tests pass
"""

import pytest

@pytest.fixture()
def setUp():
    print("\nRunning demo1 setup")

def test_methodA(setUp):
    print("Running demo1 method A")

def test_methodB(setUp):
    print("Running demo1 method B")


