def harmonic_sum(n):
    if n <= 1:
        return 0

    total = 0
    for i in range(1, n):
        total += 1 / i

    return total

# Test the function with the provided examples




def check(candidate):
    assert math.isclose(harmonic_sum(7), 2.5928571428571425, rel_tol=0.001)
    assert math.isclose(harmonic_sum(4), 2.083333333333333, rel_tol=0.001)
    assert math.isclose(harmonic_sum(19), 3.547739657143682, rel_tol=0.001)

check(harmonic_sum)