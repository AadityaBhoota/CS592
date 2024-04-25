def square_Sum(n):
    """
    Calculates the sum of squares of the first n even natural numbers.

    Args:
        n (int): The number of even natural numbers to consider.

    Returns:
        int: The sum of squares of the first n even natural numbers.
    """
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += (2 * i) ** 2
    return total_sum

def check(candidate):
    assert square_Sum(2) == 20
    assert square_Sum(3) == 56
    assert square_Sum(4) == 120

check(square_Sum)