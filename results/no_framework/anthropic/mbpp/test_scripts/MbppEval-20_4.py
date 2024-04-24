def is_woodall(x):
    """
    Checks if the given number is a Woodall number.

    A Woodall number is a number of the form 2^n - n - 1, where n is a non-negative integer.

    Examples:
    is_woodall(383) == True
    is_woodall(254) == False
    is_woodall(200) == False
    """
    n = 0
    while 2 ** n - n - 1 < x:
        n += 1
    return x == 2 ** n - n - 1

def check(candidate):
    assert is_woodall(383) == True
    assert is_woodall(254) == False
    assert is_woodall(200) == False

check(is_woodall)