def minimum(a, b):
    """
    Write a python function to find the minimum of two numbers.

    Examples:
    minimum(1, 2) == 1
    minimum(-5, -4) == -5
    minimum(0, 0) == 0

    Args:
        a (int or float): The first number to compare.
        b (int or float): The second number to compare.

    Returns:
        int or float: The minimum of the two input numbers.
    """
    if a < b:
        return a
    else:
        return b

def check(candidate):
    assert minimum(1,2) == 1
    assert minimum(-5,-4) == -5
    assert minimum(0,0) == 0

check(minimum)