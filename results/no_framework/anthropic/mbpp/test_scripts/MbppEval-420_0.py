def cube_Sum(n):
    """
    Finds the cube sum of the first n even natural numbers.

    Args:
        n (int): The number of even natural numbers to consider.

    Returns:
        int: The cube sum of the first n even natural numbers.
    """
    return n * (2 * n - 1) * (2 * n + 1) // 3

def check(candidate):
    assert cube_Sum(2) == 72
    assert cube_Sum(3) == 288
    assert cube_Sum(4) == 800

check(cube_Sum)