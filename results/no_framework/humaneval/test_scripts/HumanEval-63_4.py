def fibfib(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    fib_cache = [0, 0, 1]  # Initialize the cache with precalculated values

    for i in range(3, n+1):
        fib_cache.append(fib_cache[i-1] + fib_cache[i-2] + fib_cache[i-3])

    return fib_cache[n]

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