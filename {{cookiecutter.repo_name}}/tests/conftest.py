import importlib
import pathlib
import pytest


def pytest_collection_modifyitems(config, items):
    # python 3.4/3.5 compat: rootdir = pathlib.Path(str(config.rootdir))
    rootdir = pathlib.Path(config.rootdir)
    for item in items:
        rel_path = pathlib.Path(item.fspath).relative_to(rootdir)
        for part in rel_path.parts:
            if part.endswith('_tests'):
                mark = getattr(pytest.mark, part)
                item.add_marker(mark)

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
