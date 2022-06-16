"""Module information."""


def fib():
    """Fib."""
    ex1 = 0
    ex2 = 1

    def get_next_number():
        nonlocal ex1, ex2
        ex3 = ex1 + ex2
        ex1, ex2 = ex2, ex3
        return ex3

    return get_next_number


def fibx(number: int):
    """Fibx."""
    myfib = fib()
    if number in [0, 1]:
        return number
    for _ in range(2, number + 1):
        num = myfib()
    return num
