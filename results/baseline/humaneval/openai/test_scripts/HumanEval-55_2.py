def fib(n: int):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Test cases






METADATA = {}


def check(candidate):
    assert candidate(10) == 55
    assert candidate(1) == 1
    assert candidate(8) == 21
    assert candidate(11) == 89
    assert candidate(12) == 144


check(fib)