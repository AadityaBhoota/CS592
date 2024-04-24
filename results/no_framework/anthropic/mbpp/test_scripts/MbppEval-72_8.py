import math

def dif_Square(n):
    """
    Write a python function to check whether the given number can be represented as the difference of two squares or not.

    Examples:
    dif_Square(5) == True
    dif_Square(10) == False
    dif_Square(15) == True
    """
    for i in range(int(math.sqrt(n)) + 1):
        j = i * i
        diff = n - j
        if diff >= 0 and int(math.sqrt(diff)) ** 2 == diff:
            return True
    return False

def check(candidate):
    assert dif_Square(5) == True
    assert dif_Square(10) == False
    assert dif_Square(15) == True

check(dif_Square)