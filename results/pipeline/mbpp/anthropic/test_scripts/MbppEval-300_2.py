def count_binary_seq(n):
    if n == 1:
        return 2.0
    else:
        return 2 * (count_binary_seq(n-1)) / 2

def check(candidate):
    assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(2), 6.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(3), 20.0, rel_tol=0.001)

check(count_binary_seq)