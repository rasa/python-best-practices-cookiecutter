"""Scripts/code_format.py."""

import os
import typing as t

import pytest


def test_mypy(_: t.Any = None) -> None:
    """Test_mypy."""
    pytest.main(["--mypy", "-m", "mypy"])


def test_isort() -> None:
    """Test_isort."""
    pytest.main(["--isort", "-m", "isort"])


def test_isort_fix() -> None:
    """Test_isort_fix."""
    os.system("isort {{cookiecutter.project_module}} tests scripts")


def test_black() -> None:
    """Test_black."""
    pytest.main(["--black", "-m", "black"])


def test_black_fix() -> None:
    """Test_black_fix."""
    os.system("black {{cookiecutter.project_module}} tests scripts")


def test_pylint() -> None:
    """Test_pylint."""
    pytest.main(["--pylint", "-m", "pylint"])


def test_flake8() -> None:
    """Test_flake8."""
    pytest.main(["--flake8", "-m", "flake8"])


def pytest_cov_term() -> None:
    """Pytest_cov_term."""
    pytest.main(["--cov-report=term-missing", "--cov={{cookiecutter.project_module}}", "tests/"])


def pytest_test_reports() -> None:
    """Pytest_test_reports."""
    pytest.main(
        [
            "--isort",
            "--black",
            "--mypy",
            "--pylint",
            "--capture=sys",
            "--html=reports/code_tests/index.html",
        ]
    )


def pytest_cov_reports() -> None:
    """Pytest_cov_reports."""
    pytest.main(["--cov", "--cov-fail-under=50", "--cov-report=html:reports/code_cov/"])
