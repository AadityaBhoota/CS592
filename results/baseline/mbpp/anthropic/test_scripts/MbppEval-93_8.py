def power(a, b):
    """
    Write a function to calculate the value of 'a' to the power 'b'.

    Examples:
    power(3, 4) == 81
    power(2, 3) == 8
    power(5, 5) == 3125
    """
    return a ** b

def check(candidate):
    assert power(3,4) == 81
    assert power(2,3) == 8
    assert power(5,5) == 3125

check(power)