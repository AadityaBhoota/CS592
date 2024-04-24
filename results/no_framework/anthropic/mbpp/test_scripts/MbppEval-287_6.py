def square_Sum(n):
    """
    Calculates the sum of squares of the first n even natural numbers.

    Args:
        n (int): The number of even natural numbers to consider.

    Returns:
        int: The sum of squares of the first n even natural numbers.
    """
    return n * (n + 1) * (2 * n + 1) // 6

def check(candidate):
    assert square_Sum(2) == 20
    assert square_Sum(3) == 56
    assert square_Sum(4) == 120

check(square_Sum)