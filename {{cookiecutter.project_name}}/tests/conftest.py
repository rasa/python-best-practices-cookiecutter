"""
pytest fixtures and functions
"""
import importlib
import logging
import pathlib

import pytest

logger = logging.getLogger(__name__)


def pytest_collection_modifyitems(config, items):  # pylint: disable=invalid-name
    """
    pytest add markers dynamically based on directory name
    <directoryname>Tests
    """
    # python 3.4/3.5 compat: rootdir = pathlib.Path(str(config.rootdir))
    rootdir = pathlib.Path(config.rootdir)
    for item in items:
        relPath = pathlib.Path(item.fspath).relative_to(rootdir)
        for part in relPath.parts:
            if part.endswith("Tests"):
                mark = getattr(pytest.mark, part)
                item.add_marker(mark)


def pytest_generate_tests(metafunc):  # pylint: disable=invalid-name
    """
    If fixture begins with data_ add a parametrize fixture
    """
    for fixture in metafunc.fixturenames:
        if "data_" in fixture:
            logger.info("getting fixture=%s", fixture)
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
