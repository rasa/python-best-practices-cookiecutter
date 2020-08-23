from {{cookiecutter.project_name}}.{{cookiecutter.project_name}} import fib


def test_fib(data_fib) -> None:
    assert fib(data_fib[0]) == data_fib[1]
