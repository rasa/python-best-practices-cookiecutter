""" {{cookiecutter.project_module}}/__main__.py """
import sys

from {{cookiecutter.project_module}} import fib

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(fib.fibx(n))
