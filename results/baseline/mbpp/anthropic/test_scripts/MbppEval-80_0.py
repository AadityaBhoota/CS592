def tetrahedral_number(n):
    """
    Calculates the nth tetrahedral number.

    The tetrahedral number is a figurate number that represents a pyramid with a triangular base and three sides, all of which are triangles. It is one of the higher-dimensional extensions of the triangular number.

    The formula for the nth tetrahedral number is: (n * (n + 1) * (n + 2)) / 6.

    Args:
        n (int): The position of the tetrahedral number to calculate.

    Returns:
        float: The nth tetrahedral number.
    """
    return (n * (n + 1) * (n + 2)) / 6

def check(candidate):
    assert tetrahedral_number(5) == 35
    assert tetrahedral_number(6) == 56
    assert tetrahedral_number(7) == 84

check(tetrahedral_number)