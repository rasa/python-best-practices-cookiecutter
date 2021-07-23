"""
pytest fixtures and functions
"""
import importlib
import pathlib
import pytest


def pytestCollectionModifyItems(config, items):
    """
    pytest add markers dynamically based on directory name
    <directoryname>Test
    """
    # python 3.4/3.5 compat: rootdir = pathlib.Path(str(config.rootdir))
    rootdir = pathlib.Path(config.rootdir)
    for item in items:
        relPath = pathlib.Path(item.fspath).relative_to(rootdir)
        for part in relPath.parts:
            if part.endswith("Tests"):
                mark = getattr(pytest.mark, part)
                item.add_marker(mark)


def pytestGenerateTests(metafunc):
    """
    If fixture begins with data_ add a parametrize fixture
    """
    for fixture in metafunc.fixturenames:
        if "data_" in fixture:
            metafunc.parametrize(fixture, loadTests(fixture))


def loadTests(name):
    """
    loads test data dynamically utilizing data_<name>.py in tests/data directory
    """
    # Load module which contains test data
    testsModule = importlib.import_module("." + name, "data")
    # Tests are to be found in the variable `tests` of the module
    for test in testsModule.tests:
        yield test
