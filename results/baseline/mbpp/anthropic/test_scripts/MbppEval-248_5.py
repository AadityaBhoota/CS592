def harmonic_sum(n):
    """
    Calculates the harmonic sum of n-1.

    The harmonic sum is the sum of the reciprocals of the first n-1 positive integers.
    It is calculated as 1 + 1/2 + 1/3 + ... + 1/n.

    Args:
        n (int): The value to calculate the harmonic sum up to.

    Returns:
        float: The harmonic sum of n-1.
    """
    if n < 1:
        return 0
    else:
        return sum(1 / i for i in range(1, n))

def check(candidate):
    assert math.isclose(harmonic_sum(7), 2.5928571428571425, rel_tol=0.001)
    assert math.isclose(harmonic_sum(4), 2.083333333333333, rel_tol=0.001)
    assert math.isclose(harmonic_sum(19), 3.547739657143682, rel_tol=0.001)

check(harmonic_sum)