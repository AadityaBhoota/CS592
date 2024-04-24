def tetrahedral_number(n):
    """
    Write a function to find the nth tetrahedral number.

    Examples:
    tetrahedral_number(5) == 35.0
    tetrahedral_number(6) == 56.0
    tetrahedral_number(7) == 84.0
    """
    return (n * (n + 1) * (n + 2)) / 6

def check(candidate):
    assert tetrahedral_number(5) == 35
    assert tetrahedral_number(6) == 56
    assert tetrahedral_number(7) == 84

check(tetrahedral_number)