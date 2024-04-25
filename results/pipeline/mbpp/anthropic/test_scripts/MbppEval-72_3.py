def dif_Square(n):
    """
    Write a python function to check whether the given number can be represented as the difference of two squares or not.

    Examples:
    dif_Square(5) == True
    dif_Square(10) == False
    dif_Square(15) == True
    """
    for a in range(int(n**0.5) + 1):
        b = a + 1
        if n == a**2 - b**2:
            return True
    return False

def check(candidate):
    assert dif_Square(5) == True
    assert dif_Square(10) == False
    assert dif_Square(15) == True

check(dif_Square)