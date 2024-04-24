def harmonic_sum(n):
    """
    Calculates the harmonic sum of n-1.
    
    The harmonic sum is the sum of the reciprocals of the positive integers up to n-1.
    
    Parameters:
    n (int): The number up to which the harmonic sum will be calculated.
    
    Returns:
    float: The harmonic sum of n-1.
    """
    if n <= 0:
        return 0
    else:
        return sum(1/i for i in range(1, n))

def check(candidate):
    assert math.isclose(harmonic_sum(7), 2.5928571428571425, rel_tol=0.001)
    assert math.isclose(harmonic_sum(4), 2.083333333333333, rel_tol=0.001)
    assert math.isclose(harmonic_sum(19), 3.547739657143682, rel_tol=0.001)

check(harmonic_sum)