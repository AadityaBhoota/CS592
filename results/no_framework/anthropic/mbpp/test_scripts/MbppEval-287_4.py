def square_Sum(n):
    """
    Write a python function that takes in an integer n and returns the sum of squares of the first n even natural numbers.

    Examples:
    square_Sum(2) == 20
    square_Sum(3) == 56
    square_Sum(4) == 120
    """
    return sum(i**2 for i in range(2, 2*n+1, 2))

def check(candidate):
    assert square_Sum(2) == 20
    assert square_Sum(3) == 56
    assert square_Sum(4) == 120

check(square_Sum)