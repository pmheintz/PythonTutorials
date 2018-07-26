"""
Using pytest with command line arguments
Added pytest_addoption to conftest.py
"""

import pytest

def test_command_line_methodA(oneTimeSetUp, setUp):
    print("Running method A")

def test_command_line_methodB(oneTimeSetUp, setUp):
    print("Running method B")