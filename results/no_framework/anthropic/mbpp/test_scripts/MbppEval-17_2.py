def square_perimeter(a):
    """
    Write a function that returns the perimeter of a square given its side length as input.

    Examples:
    square_perimeter(10) == 40
    square_perimeter(5) == 20
    square_perimeter(4) == 16
    """
    return 4 * a

def check(candidate):
    assert square_perimeter(10)==40
    assert square_perimeter(5)==20
    assert square_perimeter(4)==16

check(square_perimeter)