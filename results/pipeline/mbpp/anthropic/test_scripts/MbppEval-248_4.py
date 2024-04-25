def harmonic_sum(n):
    """
    Write a function that takes in an integer n and calculates the harmonic sum of n-1.

    Examples:
    harmonic_sum(7) == 2.5928571428571425
    harmonic_sum(4) == 2.083333333333333
    harmonic_sum(19) == 3.547739657143682
    """
    harmonic_sum = 0.0
    for i in range(1, n+1):
        harmonic_sum += 1 / i
    return harmonic_sum

def check(candidate):
    assert math.isclose(harmonic_sum(7), 2.5928571428571425, rel_tol=0.001)
    assert math.isclose(harmonic_sum(4), 2.083333333333333, rel_tol=0.001)
    assert math.isclose(harmonic_sum(19), 3.547739657143682, rel_tol=0.001)

check(harmonic_sum)