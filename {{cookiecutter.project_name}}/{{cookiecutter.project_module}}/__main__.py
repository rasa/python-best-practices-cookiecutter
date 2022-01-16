import sys

from {{cookiecutter.project_module}} import fib

if __name__ == "__main__":
    n = int(sys.argv[1])
    print({{cookiecutter.project_module}}.fibx(n))
