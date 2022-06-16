""" scripts/code_format.py """

import os
import pytest


def test_mypy(_=None):
    """test_mypy"""
    pytest.main(["--mypy", "-m", "mypy"])


def test_isort():
    """test_isort"""
    pytest.main(["--isort", "-m", "isort"])


def test_isort_fix():
    """test_isort_fix"""
    os.system("isort {{cookiecutter.project_module}} tests scripts")


def test_black():
    """test_black"""
    pytest.main(["--black", "-m", "black"])


def test_black_fix():
    """test_black_fix"""
    os.system("black {{cookiecutter.project_module}} tests scripts")


def test_pylint():
    """test_pylint"""
    pytest.main(["--pylint", "-m", "pylint"])


def test_flake8():
    """test_flake8"""
    pytest.main(["--flake8", "-m", "flake8"])


def pytest_cov_term():
    """pytest_cov_term"""
    pytest.main(["--cov-report=term-missing", "--cov={{cookiecutter.project_module}}", "tests/"])


def pytest_test_reports():
    """pytest_test_reports"""
    pytest.main(
        [
            "--isort",
            "--black",
            "--mypy",
            "--pylint",
            "--capture=sys",
            "--html=reports/codeTests/index.html",
        ]
    )


def pytest_cov_reports():
    """pytest_cov_reports"""
    pytest.main(["--cov", "--cov-fail-under=50", "--cov-report=html:reports/codeCov/"])
