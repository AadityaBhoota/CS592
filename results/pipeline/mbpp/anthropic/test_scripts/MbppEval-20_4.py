def is_woodall(x):
    """
    Write a function to check if the given number is woodall or not.

    Examples:
    is_woodall(383) == True
    is_woodall(254) == False
    is_woodall(200) == False
    """
    n = 0
    while 2 ** n - 1 <= x:
        if 2 ** n - 1 == x:
            return True
        n += 1
    return False

def check(candidate):
    assert is_woodall(383) == True
    assert is_woodall(254) == False
    assert is_woodall(200) == False

check(is_woodall)