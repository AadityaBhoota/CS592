import math

def perimeter_pentagon(a):
    """
    Calculates the perimeter of a regular pentagon given the length of its sides.

    Args:
        a (float): The length of one side of the regular pentagon.

    Returns:
        float: The perimeter of the regular pentagon.
    """
    return 5 * a

def check(candidate):
    assert perimeter_pentagon(5) == 25
    assert perimeter_pentagon(10) == 50
    assert perimeter_pentagon(15) == 75

check(perimeter_pentagon)