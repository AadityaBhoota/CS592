def tetrahedral_number(n):
    """
    Calculates the nth tetrahedral number.

    The tetrahedral number T(n) is the number of balls in a tetrahedral arrangement with n balls on a side.

    Args:
        n (int): The index of the tetrahedral number to calculate.

    Returns:
        float: The nth tetrahedral number.
    """
    return (n * (n + 1) * (n + 2)) / 6

def check(candidate):
    assert tetrahedral_number(5) == 35
    assert tetrahedral_number(6) == 56
    assert tetrahedral_number(7) == 84

check(tetrahedral_number)