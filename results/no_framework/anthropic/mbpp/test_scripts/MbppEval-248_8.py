def harmonic_sum(n):
    """
    Calculates the harmonic sum of n-1.

    Args:
        n (int): The integer for which the harmonic sum is to be calculated.

    Returns:
        float: The harmonic sum of n-1.
    """
    if n <= 1:
        return 0
    else:
        return 1/n + harmonic_sum(n-1)

def check(candidate):
    assert math.isclose(harmonic_sum(7), 2.5928571428571425, rel_tol=0.001)
    assert math.isclose(harmonic_sum(4), 2.083333333333333, rel_tol=0.001)
    assert math.isclose(harmonic_sum(19), 3.547739657143682, rel_tol=0.001)

check(harmonic_sum)