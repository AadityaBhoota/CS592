def fibfib(n: int) -> int:
    """The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    """
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b, c = 0, 0, 1
        for i in range(3, n+1):
            a, b, c = b, c, a + b + c
        return c



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