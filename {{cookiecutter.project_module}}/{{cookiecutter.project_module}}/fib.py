"""
Module information
"""
def fib():
    x1 = 0
    x2 = 1
    def get_next_number():
        nonlocal x1, x2
        x3 = x1 + x2
        x1, x2 = x2, x3
        return x3
    return get_next_number

def fibx(number: int):
    myfib = fib()
    if number in [0, 1]:
        return number
    for i in range(2, number+1):
            num = myfib()
    return num
