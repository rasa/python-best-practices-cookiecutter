import os
import pytest

def mypyTests(args=None):
    pytest.main(["--mypy", "-m", "mypy"])

def isortTests():
    pytest.main(["--isort", "-m", "isort"])

def isortFix():
    os.system("isort {{cookiecutter.project_module}} tests scripts")

def blackTests():
    pytest.main(["--black", "-m", "black"])

def blackFix():
    os.system("black {{cookiecutter.project_module}} tests scripts")

def pylintTests():
    pytest.main(["--pylint", "-m", "pylint"])

def flake8Tests():
    pytest.main(["--flake8", "-m", "flake8"])

def pytestCovTerm():
    pytest.main(["--cov-report=term-missing", "--cov={{cookiecutter.project_module}}", "tests/"])

def pytestTestReports():
    pytest.main(["--isort", "--black", "--mypy", "--pylint", "--capture=sys", "--html=reports/codeTests/index.html"])

def pytestCovReports():
    pytest.main(["--cov", "--cov-fail-under=50", "--cov-report=html:reports/codeCov/"])
