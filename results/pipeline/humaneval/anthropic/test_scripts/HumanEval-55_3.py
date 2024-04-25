def fib(n: int) -> int:
    """Return the n-th Fibonacci number."""
    if n == 0:
        return 0
    if n == 1:
        return 1

    fib_list = [0, 1]
    for i in range(2, n+1):
        fib_list.append(fib_list[i-1] + fib_list[i-2])

    return fib_list[n]



METADATA = {}


def check(candidate):
    assert candidate(10) == 55
    assert candidate(1) == 1
    assert candidate(8) == 21
    assert candidate(11) == 89
    assert candidate(12) == 144


check(fib)