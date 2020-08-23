"""
Module information
"""

def fib(number: int) -> int:
    if number < 0:
        raise ValueError("fib does not allow negative numbers")
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
