"""
Module information
"""

def fib(number: int) -> int:
    if number < 0:
        raise ValueError("fib does not allow negative numbers")
    # First Fibonacci number is 0
    elif number == 1:
        return 0
    # Second Fibonacci number is 1
    elif number == 2:
        return 1
    else:
        return fib(number - 1) + fib(number - 2)
