import {{cookiecutter.project_name}}


def test_fib(data_fib) -> None:
    assert {{cookiecutter.project_name}}.fib(data_fib[0]) == data_fib[1]
