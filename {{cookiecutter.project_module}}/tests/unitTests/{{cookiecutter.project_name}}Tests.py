from {{cookiecutter.project_module}}.fib import fib


def fibTest(data_fib) -> None:
    assert fib(data_fib[0]) == data_fib[1]
