def tetrahedral_number(n):
    """
    Finds the nth tetrahedral number.

    The tetrahedral number is a figurate number that represents a pyramid with a triangular base and three sides,
    all meeting at a common vertex. The nth tetrahedral number is the sum of the first n triangular numbers.

    Args:
        n (int): The index of the tetrahedral number to calculate.

    Returns:
        float: The nth tetrahedral number.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")
    return (n * (n + 1) * (n + 2)) / 6

def check(candidate):
    assert tetrahedral_number(5) == 35
    assert tetrahedral_number(6) == 56
    assert tetrahedral_number(7) == 84

check(tetrahedral_number)