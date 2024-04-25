def fibfib(n: int) -> int:
    """
    Compute the n-th element of the FibFib number sequence.
    """
    memo = {0: 0, 1: 0, 2: 1}  # base cases

    def helper(n: int) -> int:
        if n in memo:
            return memo[n]
        memo[n] = helper(n-1) + helper(n-2) + helper(n-3)
        return memo[n]

    return helper(n)



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