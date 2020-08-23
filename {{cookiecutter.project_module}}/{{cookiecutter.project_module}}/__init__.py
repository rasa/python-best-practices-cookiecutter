"""
Module information
"""

def fib(number: int) -> int:
    if number <= 1:
        return 0
    # Second Fibonacci number is 1
    else:
        return fib(number - 1) + fib(number - 2)
