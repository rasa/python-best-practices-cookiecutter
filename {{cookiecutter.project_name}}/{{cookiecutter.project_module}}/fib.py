"""
Module information
"""


def fib():
    """fib"""
    ex1 = 0
    ex2 = 1

    def getNextNumber():
        nonlocal ex1, ex2
        ex3 = ex1 + ex2
        ex1, ex2 = ex2, ex3
        return ex3

    return getNextNumber


def fibx(number: int):
    """fibx"""
    myfib = fib()
    if number in [0, 1]:
        return number
    for _ in range(2, number + 1):
        num = myfib()
    return num
