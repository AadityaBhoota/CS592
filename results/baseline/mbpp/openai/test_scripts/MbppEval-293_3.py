def otherside_rightangle(w, h):
    """
    Calculate the length of the third side of a right-angled triangle given the lengths of the other two sides.

    Args:
    w (float): Length of one of the sides
    h (float): Length of the other side

    Returns:
    float: Length of the third side

    Examples:
    >>> otherside_rightangle(7, 8)
    10.63014581273465
    >>> otherside_rightangle(3, 4)
    5.0
    >>> otherside_rightangle(7, 15)
    16.55294535724685
    """
    return math.sqrt(w ** 2 + h ** 2)

# Test cases




def check(candidate):
    assert otherside_rightangle(7,8)==10.63014581273465
    assert otherside_rightangle(3,4)==5
    assert otherside_rightangle(7,15)==16.55294535724685

check(otherside_rightangle)