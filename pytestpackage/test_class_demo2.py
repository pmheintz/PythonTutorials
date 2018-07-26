"""
How to return a value from fixtures
"""

import pytest
from pytestpackage.class_to_test import SomeClassToTest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestClassDemo():

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.abc = SomeClassToTest(self.value)

    def test_methodA(self):
        print("Running method A")
        result = self.abc.sumNumbers(2, 8)
        assert result == 20

    def test_methodB(self):
        print("Running method B")
        result = self.abc.sumNumbers(2, 8)
        assert result > 20
