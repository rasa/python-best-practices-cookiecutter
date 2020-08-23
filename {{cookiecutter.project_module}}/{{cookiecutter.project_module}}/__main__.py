import sys

import {{cookiecutter.project_module}}

if __name__ == "__main__":
    n = int(sys.argv[1])
    print({{cookiecutter.project_module}}.fib(n))
