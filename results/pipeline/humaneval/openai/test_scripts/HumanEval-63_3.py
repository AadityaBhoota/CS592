def fibfib(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    n_minus_3, n_minus_2, n_minus_1 = 0, 0, 1

    if n in [0, 1, 2]:
        return n_minus_1

    for i in range(3, n + 1):
        fib_n = n_minus_1 + n_minus_2 + n_minus_3
        n_minus_3, n_minus_2, n_minus_1 = n_minus_2, n_minus_1, fib_n

    return fib_n



METADATA = {}


def check(candidate):
    assert candidate(2) == 1
    assert candidate(1) == 0
    assert candidate(5) == 4
    assert candidate(8) == 24
    assert candidate(10) == 81
    assert candidate(12) == 274
    assert candidate(14) == 927


check(fibfib)