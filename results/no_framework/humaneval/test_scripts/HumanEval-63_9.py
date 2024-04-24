def fibfib(n: int) -> int:
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_cache = [0, 0, 1]  # Cache to store previous fibfib values
        for i in range(3, n+1):
            fib = fib_cache[2] + fib_cache[1] + fib_cache[0]
            fib_cache[0] = fib_cache[1]
            fib_cache[1] = fib_cache[2]
            fib_cache[2] = fib
        return fib_cache[2]

# Testing the function with the provided test cases
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