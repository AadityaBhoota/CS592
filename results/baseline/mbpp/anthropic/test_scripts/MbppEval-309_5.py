def maximum(a, b):
    """
    Write a python function to find the maximum of two numbers.

    Examples:
    maximum(5, 10) == 10
    maximum(-1, -2) == -1
    maximum(9, 7) == 9
    """
    return max(a, b)

def check(candidate):
    assert maximum(5,10) == 10
    assert maximum(-1,-2) == -1
    assert maximum(9,7) == 9

check(maximum)