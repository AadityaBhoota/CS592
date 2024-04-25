def fib(n: int) -> int:
    if n < 2:
        return n
    
    fib_0 = 0
    fib_1 = 1
    for i in range(2, n+1):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
    return fib_1



METADATA = {}


def check(candidate):
    assert candidate(10) == 55
    assert candidate(1) == 1
    assert candidate(8) == 21
    assert candidate(11) == 89
    assert candidate(12) == 144


check(fib)