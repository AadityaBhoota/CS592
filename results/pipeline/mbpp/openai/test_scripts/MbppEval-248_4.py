def harmonic_sum(n):
    if not isinstance(n, int) or n <= 1:
        return "Please provide an integer greater than 1."
    
    sum_harmonic = 0
    for i in range(1, n):
        sum_harmonic += 1 / i

    return sum_harmonic

def check(candidate):
    assert math.isclose(harmonic_sum(7), 2.5928571428571425, rel_tol=0.001)
    assert math.isclose(harmonic_sum(4), 2.083333333333333, rel_tol=0.001)
    assert math.isclose(harmonic_sum(19), 3.547739657143682, rel_tol=0.001)

check(harmonic_sum)