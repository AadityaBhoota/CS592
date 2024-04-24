def fibfib(n: int, memo={0: 0, 1: 0, 2: 1}):
    if n in memo:
        return memo[n]
    else:
        memo[n] = fibfib(n-1, memo) + fibfib(n-2, memo) + fibfib(n-3, memo)
        return memo[n]

# Test cases
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24



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