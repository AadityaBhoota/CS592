def fib4(n: int) -> int:
    if n < 2:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    a, b, c, d = 0, 0, 2, 0
    for i in range(4, n + 1):
        a, b, c, d = b, c, d, a + b + c + d
    return d



METADATA = {}


def check(candidate):
    assert candidate(5) == 4
    assert candidate(8) == 28
    assert candidate(10) == 104
    assert candidate(12) == 386


check(fib4)