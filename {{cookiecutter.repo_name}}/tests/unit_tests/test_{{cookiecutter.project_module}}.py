import {{cookiecutter.project_module}}


def test_fib(data_fib) -> None:
    assert {{cookiecutter.project_module}}.fib(data_fib[0]) == data_fib[1]
