"""
Conftest - common fixtures for multiple modules or configuration for tests
run py.test -v -s test_conftest_demo*.py
"""

import pytest
from termcolor import colored, cprint

@pytest.yield_fixture()
def setUp():
    cprint("\nRunning conftest demo method setup", "cyan")
    yield
    cprint("\nRunning conftest demo method teardown", "cyan")

# Scope module will only run when the module executes
@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser, osType):

    # For command line arguements
    if browser == 'firefox':
        # This following line if for getting a value from a fixture
        value = 10
        cprint("\nRunning tests on " + str(browser), "red")
    else:
        # This following line if for getting a value from a fixture
        value = 20
        cprint("\nRunning tests on chrome", "red")

    # This following lines if for getting a value from a fixture
    if request.cls is not None:
        request.cls.value = value

    cprint("\nRunning conftest demo one time setup", "blue")
    yield value
    cprint("\nRunning conftest demo one time teardown", "blue")

# For adding command line arguments
def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

