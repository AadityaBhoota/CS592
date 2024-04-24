def harmonic_sum(n):
    if n <= 1:
        return 0
    else:
        return round(sum([1/i for i in range(1, n)]), 15)

# Test cases




def check(candidate):
    assert math.isclose(harmonic_sum(7), 2.5928571428571425, rel_tol=0.001)
    assert math.isclose(harmonic_sum(4), 2.083333333333333, rel_tol=0.001)
    assert math.isclose(harmonic_sum(19), 3.547739657143682, rel_tol=0.001)

check(harmonic_sum)