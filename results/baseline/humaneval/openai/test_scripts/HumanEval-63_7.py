def fibfib(n: int, memo={}):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    elif n in memo:
        return memo[n]

    fib_n = fibfib(n-1, memo) + fibfib(n-2, memo) + fibfib(n-3, memo)
    memo[n] = fib_n

    return fib_n

# Test cases






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