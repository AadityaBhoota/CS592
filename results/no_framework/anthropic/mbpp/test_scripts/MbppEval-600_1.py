def is_Even(n):
    """
    Write a python function to check whether the given number is even or not.

    Examples:
    is_Even(1) == False
    is_Even(2) == True
    is_Even(3) == False
    """
    return n % 2 == 0

def check(candidate):
    assert is_Even(1) == False
    assert is_Even(2) == True
    assert is_Even(3) == False

check(is_Even)