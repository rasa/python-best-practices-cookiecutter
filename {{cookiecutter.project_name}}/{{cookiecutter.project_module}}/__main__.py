""" {{cookiecutter.project_module}}/__main__.py """
# pylint: disable=C0103 # Module name "__main__" doesn't conform to camelCase naming style (invalid-name)
import sys

from {{cookiecutter.project_module}} import fib

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(fib.fibx(n))
