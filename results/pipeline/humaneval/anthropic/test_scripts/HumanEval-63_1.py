def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    """
    memo = {0: 0, 1: 0, 2: 1}  # memoization dictionary

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