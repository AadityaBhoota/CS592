def power(a, b):
    """
    Calculates the value of 'a' raised to the power of 'b'.

    Args:
        a (int or float): The base number.
        b (int): The exponent.

    Returns:
        int or float: The result of 'a' raised to the power of 'b'.
    """
    return a ** b

def check(candidate):
    assert power(3,4) == 81
    assert power(2,3) == 8
    assert power(5,5) == 3125

check(power)