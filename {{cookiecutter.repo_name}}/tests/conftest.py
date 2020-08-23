import pytest
import importlib

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if "data_" in fixture:
            metafunc.parametrize(fixture, load_tests(fixture))

def load_tests(name):
    # Load module which contains test data
    tests_module = importlib.import_module('.'+name, 'data')
    # Tests are to be found in the variable `tests` of the module
    for test in tests_module.tests:
        yield test
